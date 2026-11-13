"""Result records shared across algorithms and experiments."""

from dataclasses import dataclass

from binpack.model import Instance
from binpack.solution import Solution


@dataclass(frozen=True)
class QualityMetrics:
    """The quality indicators computed for one solution."""

    launched: int
    priority_sum: int
    served_fraction: float
    cpu_utilization: float
    ram_utilization: float
    objective_value: float
    runtime_seconds: float


@dataclass(frozen=True)
class StabilityReport:
    """The spread of launched counts and objective values across runs."""

    runs: int
    launched_mean: float
    launched_std: float
    objective_mean: float
    objective_std: float


@dataclass(frozen=True)
class AlgorithmResult:
    """One solve of one algorithm, with the seed it used and its runtime."""

    algorithm: str
    solution: Solution
    seed: int
    runtime_seconds: float


@dataclass(frozen=True)
class ExperimentRun:
    """The solves and metrics of one instance across the requested algorithms and runs."""

    instance: Instance
    results: tuple[AlgorithmResult, ...]
    metrics: tuple[QualityMetrics, ...]
