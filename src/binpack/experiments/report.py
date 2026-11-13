"""Aggregation and plotting of experiment results."""

from collections.abc import Sequence
from pathlib import Path

import pandas

from binpack.results import ExperimentRun


def summarize(runs: Sequence[ExperimentRun]) -> pandas.DataFrame:
    """Return one aggregate row per algorithm across the supplied runs."""
    raise NotImplementedError


def plot_comparison(frame: pandas.DataFrame, path: Path) -> None:
    """Write a PNG comparison plot to ``path``."""
    raise NotImplementedError
