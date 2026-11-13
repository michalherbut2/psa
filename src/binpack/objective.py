"""Objective value, count weight, and cost of a solution."""

from binpack.model import Instance
from binpack.solution import Solution


def count_weight(instance: Instance) -> float:
    """Return the weight balancing the launched count against the priority sum."""
    raise NotImplementedError


def objective_value(instance: Instance, solution: Solution) -> float:
    """Return the weighted objective value of the solution."""
    raise NotImplementedError


def cost(instance: Instance, solution: Solution) -> int:
    """Return the number of submitted containers left unlaunched."""
    raise NotImplementedError
