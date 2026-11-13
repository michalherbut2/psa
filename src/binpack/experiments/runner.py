"""Running a set of algorithms over one instance."""

from collections.abc import Sequence

from binpack.model import Instance
from binpack.results import ExperimentRun


def run_experiment(
    instance: Instance, algorithms: Sequence[str], runs: int, seed: int
) -> ExperimentRun:
    """Return the solves and metrics of every requested algorithm and run."""
    raise NotImplementedError
