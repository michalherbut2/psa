"""Quality metrics derived from a solution."""

from collections.abc import Sequence

from binpack.model import Instance
from binpack.results import QualityMetrics, StabilityReport
from binpack.solution import Solution


def evaluate(instance: Instance, solution: Solution, runtime_seconds: float) -> QualityMetrics:
    """Return the quality indicators of the solution."""
    raise NotImplementedError


def aggregate(runs: Sequence[QualityMetrics]) -> StabilityReport:
    """Return the stability report of the supplied runs."""
    raise NotImplementedError
