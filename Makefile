.PHONY: test smoke

test:
	python3 -m unittest discover -s tests -v

smoke:
	python3 ai_cli_tool.py --task "Generate release notes" --template documentation_generation
