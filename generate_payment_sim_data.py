#!/usr/bin/env python3
"""
generate_payment_sim_data.py
Creates input and output CSV files for the programmable‑money corridor simulation.
"""

import pandas as pd
from pathlib import Path

# ---------- 1. Define input parameters ----------
# Note: ASCII hyphens only (US-EU, not en‑dashes) to avoid encoding issues
corridors = ["US-EU", "US-MX", "EU-IN", "IN-SG", "AU-CN"]

input_df = pd.DataFrame({
    "corridor": corridors,
    "processing_cost_legacy_cents": [7.5] * len(corridors),
    "processing_cost_programmable_cents": [3.2] * len(corridors),
    "liquidity_buffer_legacy_pct": [1.8] * len(corridors),
    "liquidity_buffer_programmable_pct": [0.6] * len(corridors),
    "compliance_opex_legacy_bps": [7] * len(corridors),
    "compliance_opex_programmable_bps": [2] * len(corridors),
    "avg_ticket_wholesale_usd": [8400] * len(corridors),
    "avg_ticket_retail_usd": [420] * len(corridors),
    "daily_transactions": [1_000_000 / len(corridors)] * len(corridors),
    "buffer_recalc_seconds_legacy": [23 * 3600] * len(corridors),  # 23 h
    "buffer_recalc_seconds_programmable": [15] * len(corridors)
})

# ---------- 2. Define headline output metrics ----------
output_df = pd.DataFrame({
    "corridor": corridors,
    "processing_cost_reduction_pct": [57] * len(corridors),
    "working_capital_release_bp": [120] * len(corridors),
    "false_positive_reduction_pct": [67] * len(corridors),
})

# ---------- 3. Write to CSV ----------
out_dir = Path(__file__).resolve().parent
input_df.to_csv(out_dir / "payment_sim_inputs.csv", index=False)
output_df.to_csv(out_dir / "payment_sim_outputs.csv", index=False)

print("✔ CSV files created:")
print("  payment_sim_inputs.csv")
print("  payment_sim_outputs.csv")

