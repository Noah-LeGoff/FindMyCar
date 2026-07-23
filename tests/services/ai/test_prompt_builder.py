from services.ai.prompt_builder import PromptBuilder


def test_build_contains_description():
    builder = PromptBuilder()

    description = "BMW E36"

    prompt = builder.build(description)

    assert description in prompt


def test_build_returns_string():
    builder = PromptBuilder()

    prompt = builder.build("BMW")

    assert isinstance(prompt, str)


def test_prompt_contains_analysis_instructions():
    builder = PromptBuilder()

    prompt = builder.build("BMW")

    assert "maintenance items" in prompt
    assert "transparency signals" in prompt
    assert "Return structured JSON only." in prompt