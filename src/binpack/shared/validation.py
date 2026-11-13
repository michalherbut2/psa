"""Invariant checks for instances and solutions."""

from binpack.model import Instance
from binpack.solution import Solution


class ValidationError(Exception):
    """Base class for every invariant violation."""


class InvalidInstanceError(ValidationError):
    """An instance violates an invariant."""


class InvalidSolutionError(ValidationError):
    """A solution violates an invariant."""


def validate_instance(instance: Instance) -> None:
    """Raise ``InvalidInstanceError`` when the instance violates an invariant."""
    raise NotImplementedError


def validate_solution(instance: Instance, solution: Solution) -> None:
    """Raise ``InvalidSolutionError`` when the solution violates an invariant."""
    raise NotImplementedError
