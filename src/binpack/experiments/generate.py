"""Synthetic instance generation."""

from dataclasses import dataclass
from enum import Enum, auto

import numpy

from binpack.model import Instance


class LoadProfile(Enum):
    """The shape of the demand distribution."""

    CPU_HEAVY = auto()
    RAM_HEAVY = auto()
    MIXED = auto()


@dataclass(frozen=True)
class InstanceSpec:
    """The size, priority range, and load profile of an instance to generate."""

    containers: int
    nodes: int
    priority_range: tuple[int, int]
    load_profile: LoadProfile


def generate_instance(spec: InstanceSpec, rng: numpy.random.Generator) -> Instance:
    """Return an instance matching the spec."""
    raise NotImplementedError
