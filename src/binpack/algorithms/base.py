"""The algorithm contract and the timed run wrapper."""

from abc import ABC, abstractmethod

import numpy

from binpack.model import Instance
from binpack.results import AlgorithmResult
from binpack.solution import Solution


class Algorithm(ABC):
    """A solver producing one solution for an instance."""

    name: str

    @abstractmethod
    def solve(self, instance: Instance, rng: numpy.random.Generator) -> Solution:
        """Return a solution accepted by the solution invariants."""
        raise NotImplementedError


def run_algorithm(algorithm: Algorithm, instance: Instance, seed: int) -> AlgorithmResult:
    """Return the result of one timed solve."""
    raise NotImplementedError
