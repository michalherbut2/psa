"""Integration check for a reachable container daemon."""

import shutil
import subprocess

import pytest


@pytest.mark.docker
def test_container_daemon_reachable() -> None:
    """A container runs when a Docker daemon answers, and the check skips otherwise."""
    if shutil.which("docker") is None:
        pytest.skip("docker is not installed")

    probe = subprocess.run(["docker", "info"], capture_output=True, text=True, check=False)
    if probe.returncode != 0:
        pytest.skip("no container daemon is reachable")

    from testcontainers.core.container import DockerContainer

    with DockerContainer("alpine:3.20").with_command("true") as container:
        exit_code = container.get_wrapped_container().wait(timeout=60)["StatusCode"]

    assert exit_code == 0
