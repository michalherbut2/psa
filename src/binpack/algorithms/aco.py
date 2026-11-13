"""Ant colony optimization."""

import numpy

from binpack.algorithms.base import Algorithm
from binpack.model import Instance
from binpack.solution import Solution


class AntColonyOptimization(Algorithm):
    """Build placements from pheromone trails laid by earlier iterations."""

    name = "aco"

    def solve(self, instance: Instance, rng: numpy.random.Generator) -> Solution:
        """Return the best placement found by the colony."""
        raise NotImplementedError
