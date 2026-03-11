#!/usr/bin/env python3
"""Generate structured AI prompts for common development tasks."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path


def build_prompt(task: str, context: str | None = None, template: str = "task-solver") -> str:
    clean_task = task.strip()
    clean_context = context.strip() if context else "No additional context provided."

    return textwrap.dedent(
        f"""\
        # AI Development Task Prompt

        ## Objective
        Help solve the following software development task:
        {clean_task}

        ## Context
        {clean_context}

        ## Requested Output
        Please respond with the following sections:
        1. Task Summary
        2. Assumptions
        3. Recommended Approach
        4. Step-by-Step Implementation
        5. Potential Risks or Edge Cases
        6. Suggested Validation or Tests

        ## Constraints
        - Keep the response practical and developer-focused.
        - Prefer maintainable solutions over clever shortcuts.
        - Call out unclear requirements explicitly.
        - Provide code examples when useful.

        ## Preferred Template
        {template}
        """
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a structured AI prompt for a coding task."
    )
    parser.add_argument(
        "--task",
        help="The coding or documentation task you want the AI to solve.",
    )
    parser.add_argument(
        "--context",
        help="Optional technical context, stack details, or constraints.",
    )
    parser.add_argument(
        "--template",
        default="task-solver",
        help="Prompt profile label to include in the generated output.",
    )
    parser.add_argument(
        "--output",
        help="Optional file path for saving the generated prompt.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    task = args.task or input("Enter your coding task: ").strip()

    if not task:
        raise SystemExit("Error: a task is required.")

    prompt = build_prompt(task=task, context=args.context, template=args.template)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(prompt + "\n", encoding="utf-8")
        print(f"Prompt written to {output_path}")
        return 0

    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
