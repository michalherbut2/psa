"""Wall-clock timing of one call."""

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Timed[T]:
    """A call's return value paired with its elapsed wall-clock time."""

    value: T
    elapsed_seconds: float


def measure[T](call: Callable[[], T]) -> Timed[T]:
    """Return the call's value paired with the time it took."""
    raise NotImplementedError
