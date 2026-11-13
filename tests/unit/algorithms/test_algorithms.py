"""The declared algorithm classes and the registry that resolves them."""

import pytest

from binpack.algorithms import ALGORITHMS, get_algorithm
from binpack.algorithms.aco import AntColonyOptimization
from binpack.algorithms.base import Algorithm
from binpack.algorithms.ffd import FirstFitDecreasing
from binpack.algorithms.ga import GeneticAlgorithm
from binpack.algorithms.sa import SimulatedAnnealing

DECLARED_ALGORITHMS = [
    ("ffd", FirstFitDecreasing),
    ("ga", GeneticAlgorithm),
    ("sa", SimulatedAnnealing),
    ("aco", AntColonyOptimization),
]


def test_registers_every_declared_algorithm() -> None:
    assert set(ALGORITHMS) == {name for name, _ in DECLARED_ALGORITHMS}


@pytest.mark.parametrize(("name", "algorithm_class"), DECLARED_ALGORITHMS)
def test_algorithm_is_declared_with_its_name(name: str, algorithm_class: type[Algorithm]) -> None:
    algorithm = algorithm_class()

    assert isinstance(algorithm, Algorithm)
    assert algorithm.name == name


@pytest.mark.parametrize(("name", "algorithm_class"), DECLARED_ALGORITHMS)
def test_registry_resolves_each_algorithm(name: str, algorithm_class: type[Algorithm]) -> None:
    assert isinstance(ALGORITHMS[name](), algorithm_class)

    resolved = get_algorithm(name)
    assert isinstance(resolved, algorithm_class)
    assert resolved.name == name


@pytest.mark.parametrize(("name", "algorithm_class"), DECLARED_ALGORITHMS)
def test_registry_returns_a_fresh_instance(name: str, algorithm_class: type[Algorithm]) -> None:
    assert isinstance(get_algorithm(name), algorithm_class)
    assert get_algorithm(name) is not get_algorithm(name)


def test_registry_rejects_an_unknown_name() -> None:
    with pytest.raises(KeyError):
        get_algorithm("unknown")
