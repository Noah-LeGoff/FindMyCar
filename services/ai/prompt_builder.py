class PromptBuilder:
    """
    Builds prompts for AI providers.
    """

    PROMPT_VERSION = 1

    TEMPLATE = (
        "You are an automotive expert.\n\n"
        "Analyze the following vehicle description.\n\n"
        "Extract:\n"
        "- maintenance items\n"
        "- transparency signals\n"
        "- positive points\n"
        "- warning points\n"
        "- important facts\n\n"
        "Return structured JSON only.\n\n"
        "Description:\n{description}"
    )

    def build(
        self,
        description: str,
    ) -> str:
        return self.TEMPLATE.format(
            description=description,
        )