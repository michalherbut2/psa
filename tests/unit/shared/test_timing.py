"""Declared shape of the timing helper."""

import dataclasses

import pytest

from binpack.shared.timing import Timed


def test_timed_declares_fields() -> None:
    timed = Timed(value=1, elapsed_seconds=0.5)

    assert [field.name for field in dataclasses.fields(timed)] == ["value", "elapsed_seconds"]


def test_timed_is_frozen() -> None:
    timed = Timed(value=1, elapsed_seconds=0.5)

    with pytest.raises(dataclasses.FrozenInstanceError):
        timed.value = 2
