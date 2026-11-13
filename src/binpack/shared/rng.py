"""Random number generators seeded reproducibly."""

import numpy


def make_rng(seed: int) -> numpy.random.Generator:
    """Return a generator that reproduces the same stream from the seed."""
    raise NotImplementedError


def seed_sequence(seed: int, count: int) -> tuple[numpy.random.Generator, ...]:
    """Return independent generators, each reproducible from the seed alone."""
    raise NotImplementedError
