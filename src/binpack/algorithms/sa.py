"""Simulated annealing."""

import numpy

from binpack.algorithms.base import Algorithm
from binpack.model import Instance
from binpack.solution import Solution


class SimulatedAnnealing(Algorithm):
    """Improve one placement by accepting occasional worsening moves."""

    name = "sa"

    def solve(self, instance: Instance, rng: numpy.random.Generator) -> Solution:
        """Return the best placement found along the annealing schedule."""
        raise NotImplementedError
