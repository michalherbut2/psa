# Agent guide

Rules for automated agents working in this repository.

## Language

- Code, identifiers, and comments are English.
- Commit messages are English.
- `README.md` and `CONTRIBUTING.md` are Polish.
- This file is English.

## Layout

- `src/binpack` is the package; every module lives under this import root.
- `tests/unit` mirrors the package layout under `src/binpack` where a module has its own tests; batteries covering several modules sit at the tier root.
- `tests/integration` holds checks that need an external service.
- `Makefile` is the only spelling of each check.
- `pyproject.toml` carries metadata, dependencies, and tool configuration; `uv.lock` pins the resolved tree; `.python-version` pins the interpreter.

## Commands

```
uv sync
make fmt
make lint
make test
```

- `uv sync` provisions CPython 3.12 and installs both dependency groups.
- `make fmt` formats the code and is idempotent.
- `make lint` runs the static analysis and verifies formatting.
- `make test` runs the unit tier and the integration tier.

## Tests

- Every behaviour change carries a test that exercises its contract.
- Unit tests mirror the package layout and assert contracts, not implementation details.
- Integration tests carry the `docker` marker and skip when no daemon answers; a missing daemon is not a failure.
- Never make a failing check pass by editing the test to match the implementation.

## Commits

Conventional commits in the form `type(scope): description`.

The types are `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `spec`, and `plan`.
The scopes are `ENV`, `UTL`, `MOD`, `ALG`, and `EXP`.

The description states what the change does, keeps the first line under 72 characters, and never names local tooling, scratch files, or unversioned working artifacts.

## Review

- A change is ready for review only when `make lint` and `make test` pass.
- Reviewers judge the contract against the specification and never edit the code themselves.
