import torch
import numpy as np
import os
import argparse
from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt
from glob import glob
from util import get_list_distances_from_preds

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preds-dir", type=str, required=True, help="Percorso alla cartella preds/")
    parser.add_argument("--inliers-dir", type=str, required=True, help="Percorso alla cartella inliers/")
    parser.add_argument("--num-preds", type=int, default=20, help="Dimensione della shortlist")
    parser.add_argument("--tau-adaptive", type=int, required=True, help="Soglia di efficienza")
    parser.add_argument("--method-name", type=str, default=None, help="Opzionale: override nome metodo")
    return parser.parse_args()

def extract_info_from_path(preds_path):
    path = Path(preds_path)
    try:
        config_name = path.parts[-3]
    except IndexError:
        config_name = "metodo_sconosciuto"
    return config_name

def load_all_data(preds_dir, inliers_dir, num_preds):
    txt_files = sorted(glob(os.path.join(preds_dir, "*.txt")), key=lambda x: int(Path(x).stem))
    all_inlier_counts = []
    all_geo_distances = []

    print(f"Caricamento dati per {len(txt_files)} query...")
    for txt_file in tqdm(txt_files):
        distances = get_list_distances_from_preds(txt_file)[:num_preds]
        torch_file = Path(inliers_dir) / Path(txt_file).name.replace('.txt', '.torch')
        
        if not torch_file.exists(): continue
            
        results = torch.load(torch_file, weights_only=False)
        inliers = [res['num_inliers'] for res in results[:num_preds]]
        all_inlier_counts.append(inliers)
        all_geo_distances.append(distances)
        
    return all_inlier_counts, all_geo_distances

def run_safety_logic(inliers_list, dists_list, tau_adaptive, tau_ambiguity):
    cnt_safe, cnt_correct_safe = 0, 0
    for inliers, dists in zip(inliers_list, dists_list):
        if inliers[0] > tau_adaptive:
            cnt_safe += 1
            if dists[0] < 25: cnt_correct_safe += 1
        else:
            inliers_t = torch.tensor(inliers)
            sorted_inliers, indices = torch.sort(inliers_t, descending=True)
            n1 = sorted_inliers[0].item()
            n2 = sorted_inliers[1].item() if len(sorted_inliers) > 1 else 0
            rho = n2 / n1 if n1 > 0 else 1.0
            if rho < tau_ambiguity:
                cnt_safe += 1
                sorted_dists = torch.tensor(dists)[indices]
                if sorted_dists[0] < 25: cnt_correct_safe += 1
    
    coverage = cnt_safe / len(inliers_list)
    safety = cnt_correct_safe / cnt_safe if cnt_safe > 0 else 1.0
    return safety, coverage

def main():
    args = parse_arguments()
    auto_name = extract_info_from_path(args.preds_dir)
    method_display = args.method_name if args.method_name else auto_name

    inliers_list, dists_list = load_all_data(args.preds_dir, args.inliers_dir, args.num_preds)

    safety_points, coverage_points = [], []
    t_amb_range = np.arange(0.0, 1.01, 0.01)
    
    print(f"Generazione AUC per: {method_display}")
    for t_amb in tqdm(t_amb_range):
        s, c = run_safety_logic(inliers_list, dists_list, args.tau_adaptive, t_amb)
        safety_points.append(s)
        coverage_points.append(c)

    auc = np.trapz(safety_points, coverage_points)
    
    # MODIFICA: Salvataggio punti COV e SAF per il mash-up finale
    with open("risultati_finali.txt", "a") as f:
        f.write("-" * 50 + "\n")
        f.write(f"Configurazione: {method_display}\n")
        f.write(f"Tau_Adaptive: {args.tau_adaptive}\n")
        f.write(f"AUC: {abs(auc):.4f}\n")
        f.write(f"COV: {coverage_points}\n") # Lista punti asse X
        f.write(f"SAF: {safety_points}\n")      # Lista punti asse Y
        idx = (np.abs(np.array(safety_points) - 0.99)).argmin()
        f.write(f"Coverage @ 99% Safety: {coverage_points[idx]:.2%}\n")
        f.write("-" * 50 + "\n")

    # Plotting individuale
    plt.figure(figsize=(10, 6))
    plt.plot(coverage_points, safety_points, label=f'AUC: {abs(auc):.4f}', color='#1f77b4', linewidth=2.5)
    plt.axhline(y=0.99, color='red', linestyle='--', alpha=0.6, label='Safety Target 99%')
    plt.xlabel('Coverage', fontsize=12)
    plt.ylabel('Safety Rate', fontsize=12)
    plt.title(f'Safety-Coverage Curve: {method_display}', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower left')
    plt.xlim([0, 1.0])
    plt.ylim([0.7, 1.01])
    plt.tight_layout()
    
    plot_filename = f"AUC_{method_display}.png"
    plt.savefig(plot_filename, dpi=300)
    print(f"Finito. Salvato PNG e aggiornato risultati_finali.txt")

if __name__ == "__main__":
    main()