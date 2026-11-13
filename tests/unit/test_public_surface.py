"""The declared public surface: every package module imports and exposes its names."""

import importlib
import pkgutil

import pytest

import binpack

PUBLIC_SURFACE: dict[str, tuple[str, ...]] = {
    "binpack.model": ("Container", "Node", "Instance"),
    "binpack.solution": (
        "Assignment",
        "Solution",
        "Utilization",
        "is_feasible",
        "utilization",
        "node_utilization",
    ),
    "binpack.objective": ("count_weight", "objective_value", "cost"),
    "binpack.results": (
        "QualityMetrics",
        "StabilityReport",
        "AlgorithmResult",
        "ExperimentRun",
    ),
    "binpack.metrics": ("evaluate", "aggregate"),
    "binpack.shared.rng": ("make_rng", "seed_sequence"),
    "binpack.shared.timing": ("Timed", "measure"),
    "binpack.shared.validation": (
        "ValidationError",
        "InvalidInstanceError",
        "InvalidSolutionError",
        "validate_instance",
        "validate_solution",
    ),
    "binpack.shared.serialization": (
        "dump_instance",
        "load_instance",
        "dump_result",
        "load_result",
    ),
    "binpack.algorithms": ("ALGORITHMS", "get_algorithm"),
    "binpack.algorithms.base": ("Algorithm", "run_algorithm"),
    "binpack.algorithms.ffd": ("FirstFitDecreasing",),
    "binpack.algorithms.ga": ("GeneticAlgorithm",),
    "binpack.algorithms.sa": ("SimulatedAnnealing",),
    "binpack.algorithms.aco": ("AntColonyOptimization",),
    "binpack.experiments.generate": ("LoadProfile", "InstanceSpec", "generate_instance"),
    "binpack.experiments.runner": ("run_experiment",),
    "binpack.experiments.report": ("summarize", "plot_comparison"),
}


def walked_module_names() -> list[str]:
    """Return the dotted name of every module the package walk discovers."""
    return [module.name for module in pkgutil.walk_packages(binpack.__path__, "binpack.")]


def test_every_package_module_imports() -> None:
    for name in walked_module_names():
        importlib.import_module(name)


@pytest.mark.parametrize("module_name", sorted(PUBLIC_SURFACE))
def test_module_exposes_its_declared_names(module_name: str) -> None:
    module = importlib.import_module(module_name)

    assert [name for name in PUBLIC_SURFACE[module_name] if not hasattr(module, name)] == []
