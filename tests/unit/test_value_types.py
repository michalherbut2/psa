"""Declared shape of every value type in the public surface."""

import dataclasses

import pytest

from binpack.model import Container, Instance, Node
from binpack.results import (
    AlgorithmResult,
    ExperimentRun,
    QualityMetrics,
    StabilityReport,
)
from binpack.solution import Assignment, Solution, Utilization

type Record = (
    Container
    | Node
    | Instance
    | Assignment
    | Solution
    | Utilization
    | QualityMetrics
    | StabilityReport
    | AlgorithmResult
    | ExperimentRun
)

EMPTY_INSTANCE = Instance(name="empty", nodes=(), containers=())
EMPTY_SOLUTION = Solution(assignments=(), unassigned=())
EMPTY_METRICS = QualityMetrics(
    launched=0,
    priority_sum=0,
    served_fraction=0.0,
    cpu_utilization=0.0,
    ram_utilization=0.0,
    objective_value=0.0,
    runtime_seconds=0.0,
)


@pytest.mark.parametrize(
    ("value", "field_names"),
    [
        (Container(id="c1", cpu=1.5, ram=512.0, priority=3), ["id", "cpu", "ram", "priority"]),
        (
            Node(id="n1", cpu_capacity=4.0, ram_capacity=8192.0),
            ["id", "cpu_capacity", "ram_capacity"],
        ),
        (EMPTY_INSTANCE, ["name", "nodes", "containers"]),
        (Assignment(node_id="n1", container_ids=()), ["node_id", "container_ids"]),
        (EMPTY_SOLUTION, ["assignments", "unassigned"]),
        (Utilization(cpu=0.0, ram=0.0), ["cpu", "ram"]),
        (
            EMPTY_METRICS,
            [
                "launched",
                "priority_sum",
                "served_fraction",
                "cpu_utilization",
                "ram_utilization",
                "objective_value",
                "runtime_seconds",
            ],
        ),
        (
            StabilityReport(
                runs=0, launched_mean=0.0, launched_std=0.0, objective_mean=0.0, objective_std=0.0
            ),
            ["runs", "launched_mean", "launched_std", "objective_mean", "objective_std"],
        ),
        (
            AlgorithmResult(algorithm="ffd", solution=EMPTY_SOLUTION, seed=0, runtime_seconds=0.0),
            ["algorithm", "solution", "seed", "runtime_seconds"],
        ),
        (
            ExperimentRun(instance=EMPTY_INSTANCE, results=(), metrics=()),
            ["instance", "results", "metrics"],
        ),
    ],
    ids=[
        "container",
        "node",
        "instance",
        "assignment",
        "solution",
        "utilization",
        "quality_metrics",
        "stability_report",
        "algorithm_result",
        "experiment_run",
    ],
)
def test_declares_fields(value: Record, field_names: list[str]) -> None:
    assert [field.name for field in dataclasses.fields(value)] == field_names


@pytest.mark.parametrize(
    "value",
    [
        Container(id="c1", cpu=1.5, ram=512.0, priority=3),
        Node(id="n1", cpu_capacity=4.0, ram_capacity=8192.0),
        EMPTY_INSTANCE,
        Assignment(node_id="n1", container_ids=()),
        EMPTY_SOLUTION,
        Utilization(cpu=0.0, ram=0.0),
        EMPTY_METRICS,
        StabilityReport(
            runs=0, launched_mean=0.0, launched_std=0.0, objective_mean=0.0, objective_std=0.0
        ),
        AlgorithmResult(algorithm="ffd", solution=EMPTY_SOLUTION, seed=0, runtime_seconds=0.0),
        ExperimentRun(instance=EMPTY_INSTANCE, results=(), metrics=()),
    ],
    ids=[
        "container",
        "node",
        "instance",
        "assignment",
        "solution",
        "utilization",
        "quality_metrics",
        "stability_report",
        "algorithm_result",
        "experiment_run",
    ],
)
def test_is_frozen(value: Record) -> None:
    first_field = dataclasses.fields(value)[0].name
    with pytest.raises(dataclasses.FrozenInstanceError):
        setattr(value, first_field, None)


@pytest.mark.parametrize(
    ("value", "field_name"),
    [
        (EMPTY_INSTANCE, "nodes"),
        (EMPTY_INSTANCE, "containers"),
        (Assignment(node_id="n1", container_ids=()), "container_ids"),
        (EMPTY_SOLUTION, "assignments"),
        (EMPTY_SOLUTION, "unassigned"),
        (ExperimentRun(instance=EMPTY_INSTANCE, results=(), metrics=()), "results"),
        (ExperimentRun(instance=EMPTY_INSTANCE, results=(), metrics=()), "metrics"),
    ],
)
def test_holds_tuples(value: Record, field_name: str) -> None:
    assert isinstance(getattr(value, field_name), tuple)
