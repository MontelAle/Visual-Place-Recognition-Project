#!/usr/bin/env python3
"""End-to-end VPR evaluation pipeline coordinator.

This script automates a three-stage evaluation flow:

- Run `VPR-methods-evaluation/main.py` to compute retrieval predictions
    (descriptors / top-k predictions) for the configured datasets.
- For each matcher (e.g. `superpoint-lg`, `superglue`, `loftr`) run
    `match_queries_preds.py` on the saved predictions to compute geometric
    inliers between query/database images.
- Run `reranking.py` to rerank retrievals using the saved predictions and
    inliers and compute final recall values.

Usage:
    python matching_recall.py --method NAME --backbone NAME --descriptors-dimension INT [--dataset NAME] [--dry-run]

Required arguments:
    --method
    --backbone
    --descriptors-dimension

Optional arguments:
    --dataset    Restrict run to a single dataset defined in the script.
    --dry-run    Print commands instead of executing them.

Outputs:
    The evaluation script writes outputs under `logs/<log_dir>/<timestamp>/...`.
    By default this script also creates `outputs/preds` and `outputs/inliers`.
    If your project stores predictions or inliers elsewhere, adjust
    `preds_base` and `inliers_base` inside this file.
"""
import argparse
import subprocess
import sys
from pathlib import Path


def sh(cmd, dry_run=False):
    print(cmd)
    if dry_run:
        return 0
    return subprocess.run(cmd, shell=True, check=True)

def find_latest_subdir(base: Path):
    """Return the latest (newest) directory under `base`, or None if none found."""
    if not base.exists() or not base.is_dir():
        return None
    dirs = [p for p in base.iterdir() if p.is_dir()]
    if not dirs:
        return None
    # sort by modification time, newest last
    dirs.sort(key=lambda p: p.stat().st_mtime)
    return dirs[-1]

def main(dry_run=False, method=None, backbone=None, descriptors_dimension=None, dataset=None):
    py = sys.executable

    # Require explicit method/backbone/descriptors_dimension — don't run defaults
    if not method or not backbone or descriptors_dimension is None:
        print("ERROR: You must provide --method, --backbone and --descriptors-dimension.")
        sys.exit(1)
        
    # Build single method entry from provided args
    m = {
        "name": f"{method}_{backbone}",
        "method": method,
        "backbone": backbone,
        "descriptors_dimension": int(descriptors_dimension),
    }    

    # Datasets and their folder templates (adjust if your layout differs)
    datasets = {
        "tokyo_xs": {
            "db": "data/tokyo_xs/test/database",
            "queries": "data/tokyo_xs/test/queries",
        },
        "sf_xs": {
            "db": "data/sf_xs/test/database",
            "queries": "data/sf_xs/test/queries",
        },
        "svox_sun": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries_sun",
        },
        "svox_night": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries_night",
        }
    }

    # Matchers to run for each preds folder
    matchers = ["superpoint-lg", "superglue", "loftr"]

    # Common args
    num_workers = 8
    batch_size = 32
    image_size = "512 512"
    distance_metric = "L2"
    num_preds_to_save = 20
    recall_values = "1 5 10 20"

    root = Path.cwd()

    # Base folders for where to store predictions / inliers produced by scripts.
    # Adjust if your project stores them elsewhere. By default we put them under outputs/
    preds_base = root / "outputs" / "preds"
    inliers_base = root / "outputs" / "inliers"
    preds_base.mkdir(parents=True, exist_ok=True)
    inliers_base.mkdir(parents=True, exist_ok=True)    

    # If a single dataset name was passed, filter to that one
    if dataset:
        if dataset not in datasets:
            print(f"No matching dataset: {dataset}")
            return
        datasets = {dataset: datasets[dataset]}

    
    for ds_name, paths in datasets.items():
        logs_root = root / "logs"
        log_dir = f"{m['name']}_{ds_name}_{distance_metric}"

        # 1) Run main.py to get predictions
        cmd_main = (
            f"{py} VPR-methods-evaluation/main.py "
            f"--num_workers {num_workers} "
            f"--batch_size {batch_size} "
            f"--log_dir {log_dir} "
            f"--method={m['method']} --backbone={m['backbone']} --descriptors_dimension={m['descriptors_dimension']} "
            f"--image_size {image_size} "
            f"--database_folder {paths['db']} "
            f"--queries_folder {paths['queries']} "
            f"--distance_metric {distance_metric} "
            f"--num_preds_to_save {num_preds_to_save} "
            f"--recall_values {recall_values} "
            f"--save_for_uncertainty"
        )

        sh(cmd_main, dry_run=dry_run)

        # Determine where predictions were saved. The evaluation script writes to logs/<log_dir>/<timestamp>/
        # Try to find the latest timestamped folder under logs/<log_dir> and use it as preds_dir.
        logs_root = root / "logs"
        log_dir_path = logs_root / log_dir
        latest = find_latest_subdir(log_dir_path)
        if latest:
            preds_dir = latest / "preds"
        else:
            print(f"ERROR: No timestamped logs found for {log_dir} under {log_dir_path}")
            sys.exit(1)

        # 2) For each matcher, run matching on the predictions
        for matcher in matchers:
            cmd_match = (
                f"{py} match_queries_preds.py "
                f"--preds-dir '{preds_dir}' "
                f"--matcher '{matcher}' "
                f"--device 'cuda' "
                f"--num-preds {num_preds_to_save}"
            )
            sh(cmd_match, dry_run=dry_run)

            log_dir_path = logs_root / log_dir
            inliers_dir = latest / ("preds" + f"_{matcher}")

            if not inliers_dir.exists():
                print(f"ERROR: Inliers directory not found: {inliers_dir}")
                sys.exit(1)

            # 3) Run reranking using the preds and inliers
            cmd_rerank = (
                f"{py} reranking.py "
                f"--preds-dir '{preds_dir}' "
                f"--inliers-dir '{inliers_dir}' "
                f"--num-preds {num_preds_to_save} "
                f"--recall-values {recall_values}"
            )
            sh(cmd_rerank, dry_run=dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    parser.add_argument("--method", required=True, help="Method name (e.g. netvlad, mixvpr, megaloc, cosplace)")
    parser.add_argument("--backbone", required=True, help="Backbone name (e.g. VGG16, ResNet50, Dinov2)")
    parser.add_argument(
        "--descriptors-dimension",
        dest="descriptors_dimension",
        type=int,
        required=True,
        help="Descriptors dimension (integer)",
    )
    parser.add_argument("--dataset", help="Run only this dataset (e.g. tokyo_xs, sf_xs, svox)")
    args = parser.parse_args()
    main(
        dry_run=args.dry_run,
        method=args.method,
        backbone=args.backbone,
        descriptors_dimension=args.descriptors_dimension,
        dataset=args.dataset,
    )