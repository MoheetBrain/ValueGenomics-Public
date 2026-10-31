"""Extract the domestic product-by-product flow matrix from the ONS 2023 IOAT workbook.

Source: ONS, "UK input-output analytical tables - product by product", 2023 edition
(data/raw/ons_iot2023product.xlsx, Open Government Licence v3.0). Sheet "IOT" holds the
domestic use matrix (GBP million, basic prices): rows 7-110 are supplying products, columns
C-DB are using products, row 119 is total output at basic prices.

Writes data/processed/ons_iot2023_domestic_Z.csv and data/processed/ons_iot2023_products.csv.
Requires openpyxl (only for this extraction step; the experiment reads the CSVs).
"""
from __future__ import annotations

import csv
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/ons_iot2023product.xlsx"
OUT_Z = ROOT / "data/processed/ons_iot2023_domestic_Z.csv"
OUT_P = ROOT / "data/processed/ons_iot2023_products.csv"


def main() -> None:
    wb = openpyxl.load_workbook(RAW, read_only=True, data_only=True)
    rows = list(wb["IOT"].iter_rows(values_only=True))
    codes = [rows[3][j] for j in range(2, 106)]
    names = [str(rows[4][j]).strip() for j in range(2, 106)]
    row_codes = [rows[i][0] for i in range(6, 110)]
    if codes != row_codes:
        raise ValueError("row and column product codes do not match")
    z = [[float(rows[i][j] or 0) for j in range(2, 106)] for i in range(6, 110)]
    x = [float(rows[118][j]) for j in range(2, 106)]

    with OUT_Z.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["row_product_code"] + codes)
        for c, r in zip(codes, z):
            w.writerow([c] + [f"{v:.6f}" for v in r])
    with OUT_P.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["code", "name", "total_output_basic_prices_gbp_m"])
        for c, n, v in zip(codes, names, x):
            w.writerow([c, n, f"{v:.3f}"])
    print(f"{len(codes)} products; domestic intermediate use {sum(map(sum, z)):.0f}; output {sum(x):.0f} (GBP m)")


if __name__ == "__main__":
    main()
