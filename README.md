# AI Developer Productivity Tools

[![CI](https://github.com/armendujkani123/ai-dev-productivity-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/armendujkani123/ai-dev-productivity-tools/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

Open-source tools that help developers automate repetitive tasks using AI.

This repository packages prompt templates, a lightweight Python CLI, and usage examples into a small developer toolkit that can be used for code explanation, documentation generation, implementation planning, and repetitive workflow automation.

## Why This Project Exists

Developers often repeat the same prompting work across debugging, refactoring, writing docs, and reviewing unfamiliar code. This toolkit standardizes those prompts so teams can move faster with more consistent AI-assisted outputs.

## Features

- AI prompt templates for common development workflows
- CLI automation for turning a coding task into a structured AI prompt
- Code explanation helpers for understanding unfamiliar code
- Documentation generation support for README files, internal docs, and onboarding guides
- Markdown and JSON output modes for local workflows or scripting
- Reusable examples for contributors and first-time users

## Repository Structure

```text
ai-dev-productivity-tools/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── pull_request_template.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── ai_cli_tool.py
├── examples/
├── prompts/
├── pyproject.toml
└── tests/
```

## Installation

### Requirements

- Python 3.9 or newer

### Quick Start

```bash
git clone https://github.com/armendujkani123/ai-dev-productivity-tools.git
cd ai-dev-productivity-tools
python3 ai_cli_tool.py --list-templates
```

### Local Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

## Usage

Generate a structured AI prompt from a single task:

```bash
python3 ai_cli_tool.py --task "Refactor a legacy authentication module"
```

Load a task description from a file:

```bash
python3 ai_cli_tool.py --from-file examples/sample_task.txt
```

Select a different template and add technical context:

```bash
python3 ai_cli_tool.py \
  --task "Explain a slow SQL query and propose optimizations" \
  --template code_explanation \
  --context "PostgreSQL 15, 8M rows, latency spikes during peak traffic"
```

Generate machine-readable output for another script:

```bash
python3 ai_cli_tool.py \
  --task "Create onboarding docs for a new API client" \
  --template documentation_generation \
  --output-format json
```

Write the generated prompt to a file:

```bash
python3 ai_cli_tool.py \
  --task "Draft release notes for version 0.2.0" \
  --output generated/release-prompt.md
```

## Available Prompt Templates

- `task_solver`: implementation planning, refactoring, debugging, and delivery structure
- `code_explanation`: architecture explanation, onboarding, and unfamiliar code walkthroughs
- `documentation_generation`: README files, onboarding docs, feature docs, and usage instructions
- `debugging`: defect investigation, root-cause analysis, and instrumentation planning
- `test_generation`: test planning, coverage thinking, and example test scaffolds

## Example Output

The CLI produces structured prompts with:

- task objective
- project context
- response requirements
- explicit constraints
- template-specific guidance

See [sample_task.txt](./examples/sample_task.txt) and [sample_output.md](./examples/sample_output.md) for a full example.

## Quality Standards

- Tested with `unittest`
- Continuous integration on push and pull request
- MIT licensed for open-source reuse
- Contributor, security, and code-of-conduct documents included

## Roadmap

- Add prompt templates for pull request review and release planning
- Add environment variable support for custom team defaults
- Add shell completion and richer CLI formatting
- Add release automation and versioned prompt packs
- Add integration examples for GitHub Actions and local pre-commit workflows

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup, pull request expectations, and test commands.

## Security

Please report security issues according to [SECURITY.md](./SECURITY.md).

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
