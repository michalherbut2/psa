"""The registered algorithms and lookup by name."""

from collections.abc import Callable

from binpack.algorithms.aco import AntColonyOptimization
from binpack.algorithms.base import Algorithm
from binpack.algorithms.ffd import FirstFitDecreasing
from binpack.algorithms.ga import GeneticAlgorithm
from binpack.algorithms.sa import SimulatedAnnealing

ALGORITHMS: dict[str, Callable[[], Algorithm]] = {
    FirstFitDecreasing.name: FirstFitDecreasing,
    GeneticAlgorithm.name: GeneticAlgorithm,
    SimulatedAnnealing.name: SimulatedAnnealing,
    AntColonyOptimization.name: AntColonyOptimization,
}


def get_algorithm(name: str) -> Algorithm:
    """Return a freshly constructed algorithm registered under ``name``.

    Raises ``KeyError`` when the name is not registered.
    """
    return ALGORITHMS[name]()
