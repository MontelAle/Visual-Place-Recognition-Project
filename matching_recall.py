#!/usr/bin/env python3
"""Orchestrate VPR experiments: run methods on datasets, run matchers, then reranking.

Usage: python matching_recall.py [--dry-run]

This script mirrors the commands currently in the notebook and organizes
outputs by log_dir names. It runs sequentially; use --dry-run to print commands
without executing them. If your project saves predictions or inliers in different
locations, set `preds_base` and `inliers_base` variables or pass args (TODO).
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

def main(dry_run=False, method=None, dataset=None):
    py = sys.executable

    # Describe the models (as in your notebook)
    methods = [
        {"name": "netvlad_VGG16", "method": "netvlad", "backbone": "VGG16", "descriptors_dimension": 4096},
        {"name": "mixvpr_ResNet50", "method": "mixvpr", "backbone": "ResNet50", "descriptors_dimension": 4096},
        {"name": "megaloc_Dinov2", "method": "megaloc", "backbone": "Dinov2", "descriptors_dimension": 8448},
        {"name": "cosplace_ResNet50", "method": "cosplace", "backbone": "ResNet50", "descriptors_dimension": 2048},
    ]

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
        "svox": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries",
        },
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

    # If a single method name was passed, filter to that one
    if method:
        methods = [m for m in methods if m["method"] == method]
        if not methods:
            print(f"No matching method definition for: {method}")
            return

    # If a single dataset name was passed, filter to that one
    if dataset:
        if dataset not in datasets:
            print(f"No matching dataset: {dataset}")
            return
        datasets = {dataset: datasets[dataset]}

    for m in methods:
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
    parser.add_argument("--method", help="Run only this method (e.g. netvlad, mixvpr, megaloc, cosplace)")
    parser.add_argument("--dataset", help="Run only this dataset (e.g. tokyo_xs, sf_xs, svox)")
    args = parser.parse_args()
    main(dry_run=args.dry_run, method=args.method, dataset=args.dataset)