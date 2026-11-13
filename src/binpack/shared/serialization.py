"""JSON persistence for instances and experiment runs."""

from pathlib import Path

from binpack.model import Instance
from binpack.results import ExperimentRun


def dump_instance(instance: Instance, path: Path) -> None:
    """Write the instance to ``path`` as a JSON document."""
    raise NotImplementedError


def load_instance(path: Path) -> Instance:
    """Read an instance from the JSON document at ``path``."""
    raise NotImplementedError


def dump_result(run: ExperimentRun, path: Path) -> None:
    """Write the experiment run to ``path`` as a JSON document."""
    raise NotImplementedError


def load_result(path: Path) -> ExperimentRun:
    """Read an experiment run from the JSON document at ``path``."""
    raise NotImplementedError
