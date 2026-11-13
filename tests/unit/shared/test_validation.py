"""Declared exception hierarchy of the validation helper."""

import pytest

from binpack.shared.validation import (
    InvalidInstanceError,
    InvalidSolutionError,
    ValidationError,
)


@pytest.mark.parametrize(
    ("error", "base"),
    [
        (InvalidInstanceError, ValidationError),
        (InvalidSolutionError, ValidationError),
        (ValidationError, Exception),
    ],
    ids=["invalid_instance", "invalid_solution", "validation"],
)
def test_exception_hierarchy(error: type[Exception], base: type[Exception]) -> None:
    assert issubclass(error, base)
