"""Solution value types, feasibility, and utilisation."""

from dataclasses import dataclass

from binpack.model import Instance


@dataclass(frozen=True)
class Assignment:
    """The containers launched on one node."""

    node_id: str
    container_ids: tuple[str, ...]


@dataclass(frozen=True)
class Solution:
    """A placement: per-node assignments plus the containers left unlaunched."""

    assignments: tuple[Assignment, ...]
    unassigned: tuple[str, ...]


@dataclass(frozen=True)
class Utilization:
    """The fraction of CPU and RAM consumed, each in ``[0, 1]``."""

    cpu: float
    ram: float


def is_feasible(instance: Instance, solution: Solution) -> bool:
    """Report whether the solution is accepted by the solution invariants."""
    raise NotImplementedError


def utilization(instance: Instance, solution: Solution) -> Utilization:
    """Return the cluster-wide fraction of CPU and RAM consumed."""
    raise NotImplementedError


def node_utilization(instance: Instance, solution: Solution, node_id: str) -> Utilization:
    """Return the fraction of CPU and RAM consumed on one node."""
    raise NotImplementedError
