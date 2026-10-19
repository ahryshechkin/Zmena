## Zmena

Thank you for your interest in contributing to **Zmena**!  
We welcome bug reports, feature requests, documentation improvements, and code contributions.

Please take a moment to read this guide before opening an issue or pull request. This guide explains the basic workflow,
environment configuration, hook setup, naming conventions, and rules to help keep changes consistent and easy to review.

The project uses [**uv**](https://docs.astral.sh/uv/) for Python version, virtual environment, and dependency
management. Run project commands within the managed environment using `uv run`.


## Basic Workflow

1. Fork the repository
2. Configure the development environment
3. Set up hooks (if they are not configured yet)
4. Create a new branch from `main`
5. Make your changes
6. Open a pull request

### Before You Develop

After installing **uv**, navigate to the project root folder, create a virtual environment, and install all dependencies
from `uv.lock`:
```
uv sync
```

Do not install or update project dependencies manually with `pip`. To add or remove a dependency, use `uv add` or
`uv remove` and commit the changes to both `pyproject.toml` and `uv.lock`. Configure pre-commit hooks to keep the
codebase clean and consistent. Hooks are configured in `.pre-commit-config.yaml`. Run hooks before opening a pull
request. If a hook fails, fix the reported issue and run it again.

### Hook Installation
```
uv run pre-commit install
```

### Manual Hook Execution
```
uv run pre-commit run --all-files
```


## Naming Convention

### Pull Request

Pull request follows this title pattern:
```
[ZM-< issue-id >] Short Description
```

Examples:
- [ZM-0001] New Parser
- [ZM-0002] Empty Input

Guidelines:
- Describe what was changed
- Explain why it was changed (optional)

### Branch Name

Branch name should be in the format:
```
zm-< issue-id >-short-description
```

Examples:
- zm-0001-new-parser
- zm-0002-empty-input

Guidelines:
- Use lowercase letters and hyphens only
- Avoid spaces or special characters

### Commit Message

This project complies with the following convention:
```
< type >: short description
```

Allowed types:
- `feat` - add a new feature or enhancement
- `fix` - fix a bug
- `test` - add or update tests
- `refactor` - improve code structure or readability without changing functionality
- `docs` - add or update documentation
- `chore` - maintain the project infrastructure

Examples:
- `feat`: add base parser interface
- `fix`: handle empty input
- `test`: add parser unit tests
- `refactor`: extract common logic
- `docs`: add parser usage example
- `chore`: upgrade dependency versions

Guidelines:
- Use **imperative mood** (`add`, `handle`, `extract`)
- Keep commits focused and meaningful
- Avoid mixing unrelated changes in one commit
