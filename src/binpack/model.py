"""Domain value types for containers, nodes, and instances."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Container:
    """A workload unit with CPU and RAM demands and a priority."""

    id: str
    cpu: float
    ram: float
    priority: int


@dataclass(frozen=True)
class Node:
    """A cluster node with a fixed CPU and RAM capacity."""

    id: str
    cpu_capacity: float
    ram_capacity: float


@dataclass(frozen=True)
class Instance:
    """A cluster and the containers submitted to it."""

    name: str
    nodes: tuple[Node, ...]
    containers: tuple[Container, ...]
