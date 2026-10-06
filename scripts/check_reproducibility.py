#!/usr/bin/env python3
"""Verify deterministic regeneration of the committed synthetic dataset and example outputs."""
from __future__ import annotations

from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

TRACKED = [
    ROOT / "data" / "sample_pharmacy_products.csv",
    ROOT / "outputs" / "kpi_summary.csv",
    ROOT / "outputs" / "category_analysis.csv",
    ROOT / "outputs" / "supplier_analysis.csv",
    ROOT / "outputs" / "single_supplier_dependency.csv",
    ROOT / "outputs" / "zero_sales_risk.csv",
    ROOT / "outputs" / "top20_by_sales_qty.csv",
    ROOT / "outputs" / "top20_by_profit.csv",
    ROOT / "outputs" / "validation_summary.csv",
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    original = {path: path.read_bytes() for path in TRACKED}
    generator = load_module("generate_synthetic_data", SCRIPTS / "generate_synthetic_data.py")
    builder = load_module("build_example_outputs", SCRIPTS / "build_example_outputs.py")

    changed: list[str] = []
    try:
        generator.main()
        builder.main()

        for path, before in original.items():
            after = path.read_bytes()
            if after != before:
                changed.append(str(path.relative_to(ROOT)))
    finally:
        for path, before in original.items():
            path.write_bytes(before)

    if changed:
        print("ERROR: deterministic regeneration differs from committed artifacts:")
        for rel in changed:
            print(f" - {rel}")
        sys.exit(1)

    print("REPRODUCIBILITY PASS")
    print("PASS | fixed-seed synthetic CSV regeneration")
    print("PASS | checked-in analytical outputs regeneration")


if __name__ == "__main__":
    main()
