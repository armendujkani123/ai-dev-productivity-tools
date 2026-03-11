import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import ai_cli_tool


class AICLIToolTests(unittest.TestCase):
    def test_list_templates_includes_default_template(self) -> None:
        self.assertIn("task_solver", ai_cli_tool.list_templates())

    def test_load_template_raises_for_unknown_name(self) -> None:
        with self.assertRaises(ValueError):
            ai_cli_tool.load_template("missing_template")

    def test_build_prompt_payload_contains_expected_fields(self) -> None:
        payload = ai_cli_tool.build_prompt_payload(
            task="Explain this Flask app",
            context="Python 3.11",
            template="code_explanation",
            audience="backend engineer",
        )
        self.assertEqual(payload["preferred_template"], "code_explanation")
        self.assertIn("backend engineer", payload["objective"])
        self.assertIn("Python 3.11", payload["context"])
        self.assertIn("What the code does", payload["template_guidance"])

    def test_main_lists_templates(self) -> None:
        buffer = StringIO()
        with redirect_stdout(buffer):
            exit_code = ai_cli_tool.main(["--list-templates"])
        self.assertEqual(exit_code, 0)
        self.assertIn("documentation_generation", buffer.getvalue())

    def test_main_can_render_json(self) -> None:
        buffer = StringIO()
        with redirect_stdout(buffer):
            exit_code = ai_cli_tool.main(
                ["--task", "Write docs", "--output-format", "json"]
            )
        self.assertEqual(exit_code, 0)
        parsed = json.loads(buffer.getvalue())
        self.assertEqual(parsed["preferred_template"], "task_solver")
        self.assertIn("Write docs", parsed["objective"])

    def test_main_can_read_task_from_file_and_write_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            task_file = Path(tmpdir) / "task.txt"
            output_file = Path(tmpdir) / "prompt.md"
            task_file.write_text("Review this CLI design", encoding="utf-8")

            buffer = StringIO()
            with redirect_stdout(buffer):
                exit_code = ai_cli_tool.main(
                    [
                        "--from-file",
                        str(task_file),
                        "--output",
                        str(output_file),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_file.exists())
            self.assertIn("Prompt written to", buffer.getvalue())
            self.assertIn("Review this CLI design", output_file.read_text(encoding="utf-8"))

    def test_parse_args_supports_version_flag(self) -> None:
        with self.assertRaises(SystemExit) as exc:
            ai_cli_tool.parse_args(["--version"])
        self.assertEqual(exc.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
