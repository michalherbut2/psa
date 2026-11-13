"""Genetic algorithm."""

import numpy

from binpack.algorithms.base import Algorithm
from binpack.model import Instance
from binpack.solution import Solution


class GeneticAlgorithm(Algorithm):
    """Evolve a population of placements through selection, crossover, and mutation."""

    name = "ga"

    def solve(self, instance: Instance, rng: numpy.random.Generator) -> Solution:
        """Return the best placement found by the population."""
        raise NotImplementedError
