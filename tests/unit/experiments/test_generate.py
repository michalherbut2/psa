"""The declared generation types."""

from binpack.experiments.generate import LoadProfile


def test_declares_every_load_profile() -> None:
    assert {profile.name for profile in LoadProfile} == {"CPU_HEAVY", "RAM_HEAVY", "MIXED"}
