# edition_engine.py — FastPath Whole-File Replacement
# Clarity Companion — Edition Engine (v1)

from typing import Dict, Callable

class EditionEngine:
    """
    Edition Engine
    Applies stylistic transformations to a completed lesson.
    Editions modify tone, density, structure, or style.
    """

    def __init__(self):
        self.version = "1.0"
        self.registry: Dict[str, Callable[[str], str]] = {}
        self._register_default_editions()

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------
    def register(self, name: str, transform: Callable[[str], str]):
        """
        Registers a new edition transform.
        """
        self.registry[name] = transform

    def _register_default_editions(self):
        """
        Registers the built-in edition transforms.
        """

        # Concise Edition
        def concise(text: str) -> str:
            lines = text.split("\n")
            trimmed = [line for line in lines if len(line.strip()) > 0]
            return "\n".join(trimmed[: max(3, len(trimmed) // 3)])

        # Expanded Edition
        def expanded(text: str) -> str:
            return (
                "## Expanded Edition\n"
                "This version adds more detail, elaboration, and connective tissue.\n\n"
                + text
                + "\n\n(End of expanded edition)"
            )

        # Conversational Edition
        def conversational(text: str) -> str:
            return (
                "## Conversational Edition\n"
                "Let's walk through this together in a more relaxed tone.\n\n"
                + text.replace("###", "####")
                + "\n\n(End of conversational edition)"
            )

        # Poetic Edition
        def poetic(text: str) -> str:
            return (
                "## Poetic Edition\n"
                "A softer, more lyrical rendering of the lesson:\n\n"
                + text.replace(".", ".\n")
                + "\n(End of poetic edition)"
            )

        # Technical Edition
        def technical(text: str) -> str:
            return (
                "## Technical Edition\n"
                "A more formal, precise, and specification-like rendering:\n\n"
                + text.upper()
                + "\n(End of technical edition)"
            )

        # Beginner Edition
        def beginner(text: str) -> str:
            return (
                "## Beginner Edition\n"
