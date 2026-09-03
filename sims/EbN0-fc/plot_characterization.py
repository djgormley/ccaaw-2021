#!/usr/bin/env python3
"""Recreate the corrected center-frequency characterization figure."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


FCW_BINS = list(range(-32768, 32753, 3276))
DISPLAY_MHZ = [round(-0.50 + 0.05 * index, 2) for index in range(21)]
NOMINAL_EBN0_DB = [12, 9, 6, 3, 0]
TRIALS = 300


def marker_area(proportion: float) -> float:
    """Return a visible marker area in points squared."""

    return 7.0 + 125.0 * proportion


def load_proportions(data_dir: Path) -> list[list[float]]:
    rows: list[list[float]] = []
    known_bins = set(FCW_BINS)

    for index in range(1, 6):
        path = data_dir / f"fc_{index}.txt"
        values = [int(value) for value in path.read_text(encoding="ascii").split()]
        if len(values) != TRIALS:
            raise ValueError(f"{path} contains {len(values)} records; expected {TRIALS}")

        unmatched = Counter(value for value in values if value not in known_bins)
        if set(unmatched) - {0}:
            raise ValueError(f"{path} contains unexpected FCWs: {sorted(unmatched)}")

        counts = Counter(values)
        rows.append(
            [counts[fcw] / TRIALS for fcw in FCW_BINS]
            + [counts[0] / TRIALS]
        )

    return rows


def plot(data_dir: Path, output: Path) -> None:
    proportions = load_proportions(data_dir)
    frequency_positions = list(range(len(FCW_BINS)))
    unmatched_position = len(FCW_BINS) + 1.5

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Nimbus Roman", "Times New Roman", "DejaVu Serif"],
            "font.size": 8,
            "axes.labelsize": 8.5,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
        }
    )

    figure, axis = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
    for row_index, nominal_ebn0 in enumerate(NOMINAL_EBN0_DB):
        row = proportions[row_index]
        for position, proportion in zip(frequency_positions + [unmatched_position], row):
            if proportion == 0:
                continue
            axis.scatter(
                position,
                nominal_ebn0,
                s=marker_area(proportion),
                facecolor="0.20",
                edgecolor="black",
                linewidth=0.35,
                zorder=3,
            )

    axis.axvline(len(FCW_BINS) + 0.6, color="0.45", linewidth=0.7, linestyle="--")
    axis.set_xlim(-0.8, unmatched_position + 0.8)
    axis.set_ylim(-1.6, 13.6)
    axis.set_yticks(NOMINAL_EBN0_DB)
    axis.set_ylabel(r"Nominal $E_b/N_0$ (dB)")

    tick_indices = [0, 5, 10, 15, 20]
    axis.set_xticks(tick_indices + [unmatched_position])
    axis.set_xticklabels(
        [f"{DISPLAY_MHZ[index]:.2f}" for index in tick_indices] + ["literal\nFCW 0"]
    )
    axis.set_xlabel("Displayed center-frequency estimate (MHz)")
    axis.grid(axis="y", color="0.86", linewidth=0.6)
    axis.set_axisbelow(True)

    legend_proportions = [0.01, 0.10, 0.50, 1.00]
    handles = [
        axis.scatter(
            [],
            [],
            s=marker_area(proportion),
            facecolor="0.20",
            edgecolor="black",
            linewidth=0.35,
            label=f"{proportion:.0%}",
        )
        for proportion in legend_proportions
    ]
    axis.legend(
        handles=handles,
        title="Trial proportion (marker area)",
        ncol=4,
        loc="lower center",
        bbox_to_anchor=(0.5, 1.0),
        frameon=False,
        columnspacing=1.0,
        handletextpad=0.35,
        borderaxespad=0.15,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(
        output,
        dpi=600,
        facecolor="white",
        metadata={
            "Title": "Center-frequency characterization records",
            "Description": (
                "Trial proportions for retained center-frequency records at nominal "
                "12, 9, 6, 3, and 0 dB settings; unmatched literal FCW zero records "
                "are displayed separately."
            ),
        },
    )
    plt.close(figure)


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=script_dir)
    parser.add_argument(
        "--output",
        type=Path,
        default=script_dir.parents[1] / "images" / "EbN0_fc_histo.png",
    )
    arguments = parser.parse_args()
    plot(arguments.data_dir, arguments.output)


if __name__ == "__main__":
    main()
