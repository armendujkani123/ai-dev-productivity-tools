# Contributing

Thank you for contributing to AI Developer Productivity Tools.

## Development Setup

```bash
git clone https://github.com/armendujkani123/ai-dev-productivity-tools.git
cd ai-dev-productivity-tools
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
```

## Running Tests

```bash
python3 -m unittest discover -s tests -v
```

## Pull Request Guidelines

- Keep pull requests focused and easy to review
- Add or update tests for behavior changes
- Update documentation when CLI flags or prompt templates change
- Use clear commit messages and explain the user impact in the pull request

## Reporting Issues

Open a GitHub issue with:

- your Python version
- the command you ran
- the observed behavior
- the expected behavior
- a small reproducible example when possible
