# conversation_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Conversation (v1)

from typing import List, Dict

class ConversationPack:
    """
    Domain Pack: Conversation
    Provides conversational learning structures, reflective prompts,
    and lightweight guidance suitable for general dialogue-based lessons.
    """

    def __init__(self):
        self.domain_name = "conversation"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a conversation-style lesson.
        """
        return [
            {
                "title": "Let’s Talk About " + topic,
                "content": f"This section introduces the topic in a friendly, conversational tone. "
                           f"We explore what '{topic}' means and why it matters in everyday life."
            },
            {
                "title": "A Simple Breakdown",
                "content": f"Here we break '{topic}' into simple, relatable ideas. "
                           f"No jargon, no complexity — just clarity."
            },
            {
                "title": "A Question to Reflect On",
                "content": f"Think about this: How does '{topic}' show up in your daily experiences? "
                           f"What does it mean to you personally?"
            },
            {
                "title": "A Practical Example",
                "content": f"Imagine a real-life situation where '{topic}' becomes important. "
                           f"This example helps make the idea concrete and easy to understand."
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Conversation pack uses a soft, reflective tone.
        """
        return "reflective"

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------
    def get_metadata(self) -> Dict:
        return {
            "domain": self.domain_name,
            "version": self.version
        }

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def generate(self, topic: str) -> Dict:
        """
        Main method called by the engine.
        Returns a structured lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
