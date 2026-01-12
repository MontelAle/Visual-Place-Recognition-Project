import torch
import numpy as np
import os
import argparse
from pathlib import Path
from glob import glob
from tqdm import tqdm
from util import get_list_distances_from_preds

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preds-dir", type=str, required=True, help="Path a preds/ di SF-XS Val")
    parser.add_argument("--inliers-dir", type=str, required=True, help="Path a inliers/ di SF-XS Val")
    args = parser.parse_args()

    txt_files = sorted(glob(os.path.join(args.preds_dir, "*.txt")), key=lambda x: int(Path(x).stem))
    
    inlier_thresholds = np.arange(0, 300, 10) # partiziona in bin fino a 300 inliers
    results = {t: {"correct": 0, "total": 0} for t in inlier_thresholds}

    print("Analisi SF-XS Val per calibrazione Tau_Adaptive...")
    for txt_file in tqdm(txt_files):
        # Ground Truth distance del primo classificato
        dists = get_list_distances_from_preds(txt_file)
        if len(dists) == 0: continue
        is_correct = dists[0] < 25

        # Inlier del primo classificato (n1 del retrieval)
        torch_file = Path(args.inliers_dir) / Path(txt_file).name.replace('.txt', '.torch')
        if not torch_file.exists(): continue
        
        inliers_data = torch.load(torch_file, weights_only=False) ## carica il numero di inliers
        n1_retrieval = inliers_data[0]['num_inliers']

        # Aggiorna i bin
        for t in inlier_thresholds:
            if n1_retrieval >= t:
                results[t]["total"] += 1
                if is_correct:
                    results[t]["correct"] += 1

    print("\n RISULTATI CALIBRAZIONE ") ## da qui si calcola per ogni bin la percentuale (corrette/totali) e poi si prende il primmo che abbia una precision= 99
    recommended_tau = None
    for t in inlier_thresholds:
        res = results[t]
        if res["total"] > 0:
            acc = res["correct"] / res["total"]
            print(f"Inlier >= {t:3}: Precision {acc:.2%} (Supporto: {res['total']} query)")
            if acc >= 0.99 and recommended_tau is None:
                recommended_tau = t

    print(f"\n>>> SOGLIA CONSIGLIATA (Tau_Adaptive): {recommended_tau}")

if __name__ == "__main__":
    main()