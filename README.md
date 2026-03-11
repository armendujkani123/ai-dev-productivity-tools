# AI Developer Productivity Tools

Open-source tools that help developers automate repetitive tasks using AI.

## Features

- AI prompt templates for common development workflows
- CLI automation for turning a coding task into a structured AI prompt
- Code explanation helpers for understanding unfamiliar code
- Documentation generation prompts for faster project writing

## Repository Structure

```text
ai-dev-productivity-tools/
├── LICENSE
├── README.md
├── ai_cli_tool.py
├── examples/
│   ├── sample_output.md
│   └── sample_task.txt
└── prompts/
    ├── code_explanation.md
    ├── documentation_generation.md
    └── task_solver.md
```

## Installation

### Requirements

- Python 3.9+

### Quick Start

```bash
git clone https://github.com/<your-username>/ai-dev-productivity-tools.git
cd ai-dev-productivity-tools
python3 ai_cli_tool.py --help
```

### Optional

Make the CLI executable:

```bash
chmod +x ai_cli_tool.py
./ai_cli_tool.py --task "Write unit tests for a Flask endpoint"
```

## Usage

Generate a structured AI prompt from a development task:

```bash
python3 ai_cli_tool.py --task "Refactor a legacy authentication module"
```

Add technical context:

```bash
python3 ai_cli_tool.py \
  --task "Explain a slow SQL query and propose optimizations" \
  --context "PostgreSQL 15, table has 8M rows, latency spikes during peak traffic"
```

Write the generated prompt to a file:

```bash
python3 ai_cli_tool.py \
  --task "Create onboarding docs for a new API client" \
  --output prompts/generated_prompt.md
```

## Prompt Templates

The `prompts/` directory contains reusable templates for:

- Solving coding tasks
- Explaining code
- Generating documentation

These templates can be adapted for ChatGPT, Codex, Claude, or other AI assistants.

## Examples

See the `examples/` directory for:

- A sample task input
- A sample generated prompt

## Roadmap

- Add prompt templates for debugging and test generation
- Support template selection from the CLI
- Export prompts as Markdown or JSON
- Add shell wrappers for CI and team workflows

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Make focused changes with clear documentation
4. Open a pull request with a concise description

Issues and suggestions are also welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
