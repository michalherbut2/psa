"""First Fit Decreasing, the greedy baseline."""

import numpy

from binpack.algorithms.base import Algorithm
from binpack.model import Instance
from binpack.solution import Solution


class FirstFitDecreasing(Algorithm):
    """Place each container, largest demand first, on the first node that fits."""

    name = "ffd"

    def solve(self, instance: Instance, rng: numpy.random.Generator) -> Solution:
        """Return the greedy placement."""
        raise NotImplementedError
