#!/usr/bin/env python3
"""Generate structured AI prompts for common development tasks."""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

DEFAULT_TEMPLATE = "task_solver"
DEFAULT_AUDIENCE = "software engineer"
VERSION = "0.1.0"


def template_dir() -> Path:
    return Path(__file__).resolve().parent / "prompts"


def list_templates() -> list[str]:
    return sorted(path.stem for path in template_dir().glob("*.md"))


def load_template(template_name: str) -> str:
    template_path = template_dir() / f"{template_name}.md"
    if not template_path.exists():
        available = ", ".join(list_templates()) or "none"
        raise ValueError(
            f"Unknown template '{template_name}'. Available templates: {available}."
        )
    return template_path.read_text(encoding="utf-8").strip()


def read_task(task: str | None, from_file: str | None) -> str:
    if task and from_file:
        raise ValueError("Use either --task or --from-file, not both.")
    if from_file:
        return Path(from_file).read_text(encoding="utf-8").strip()
    if task:
        return task.strip()
    return input("Enter your coding task: ").strip()


def build_prompt_payload(
    *,
    task: str,
    context: str | None = None,
    template: str = DEFAULT_TEMPLATE,
    audience: str = DEFAULT_AUDIENCE,
) -> dict[str, str]:
    clean_task = task.strip()
    clean_context = context.strip() if context else "No additional context provided."
    template_guidance = load_template(template)

    return {
        "title": "AI Development Task Prompt",
        "objective": f"Help a {audience} solve the following task:\n{clean_task}",
        "context": clean_context,
        "requested_output": (
            "1. Task Summary\n"
            "2. Assumptions\n"
            "3. Recommended Approach\n"
            "4. Step-by-Step Implementation\n"
            "5. Potential Risks or Edge Cases\n"
            "6. Suggested Validation or Tests"
        ),
        "constraints": (
            "- Keep the response practical and developer-focused.\n"
            "- Prefer maintainable solutions over clever shortcuts.\n"
            "- Call out unclear requirements explicitly.\n"
            "- Provide code examples when useful."
        ),
        "preferred_template": template,
        "template_guidance": template_guidance,
    }


def render_markdown(payload: dict[str, str]) -> str:
    return textwrap.dedent(
        f"""\
        # {payload["title"]}

        ## Objective
        {payload["objective"]}

        ## Context
        {payload["context"]}

        ## Requested Output
        {payload["requested_output"]}

        ## Constraints
        {payload["constraints"]}

        ## Preferred Template
        {payload["preferred_template"]}

        ## Template Guidance
        {payload["template_guidance"]}
        """
    ).strip()


def render_prompt(payload: dict[str, str], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(payload, indent=2)
    return render_markdown(payload)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a structured AI prompt for a coding task."
    )
    parser.add_argument(
        "--task",
        help="The coding or documentation task you want the AI to solve.",
    )
    parser.add_argument(
        "--from-file",
        help="Read the task description from a text or markdown file.",
    )
    parser.add_argument(
        "--context",
        help="Optional technical context, stack details, or constraints.",
    )
    parser.add_argument(
        "--template",
        default=DEFAULT_TEMPLATE,
        help="Prompt template to use. Run --list-templates to inspect options.",
    )
    parser.add_argument(
        "--audience",
        default=DEFAULT_AUDIENCE,
        help="Primary audience for the AI response.",
    )
    parser.add_argument(
        "--output-format",
        default="markdown",
        choices=("markdown", "json"),
        help="Format for the generated prompt.",
    )
    parser.add_argument(
        "--output",
        help="Optional file path for saving the generated prompt.",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available prompt templates and exit.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.list_templates:
        for name in list_templates():
            print(name)
        return 0

    try:
        task = read_task(args.task, args.from_file)
        if not task:
            raise ValueError("A task is required.")
        payload = build_prompt_payload(
            task=task,
            context=args.context,
            template=args.template,
            audience=args.audience,
        )
        rendered = render_prompt(payload, args.output_format)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"Error: {exc}") from exc

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
        print(f"Prompt written to {output_path}")
        return 0

    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
