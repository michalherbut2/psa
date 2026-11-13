"""Smoke test for the installed package."""

import binpack


def test_package_imports() -> None:
    """The distribution installs and its import root resolves."""
    assert binpack.__name__ == "binpack"
