"""
Lesson Sections — turns architecture into concrete section objects.
Full content generation version.
"""

from typing import List, Dict


class LessonSectionsBuilder:
    def build_sections(self, architecture: List[Dict[str, str]], topic: str) -> List[Dict[str, str]]:
        """
        Given an architecture and a topic string, return concrete sections:
        [{ "id": ..., "title": ..., "content": ... }, ...]
        """

        sections = []
        for spec in architecture:
            section_id = spec["id"]
            section = {
                "id": section_id,
                "title": spec["title"],
                "content": self.generate_section_content(section_id, topic),
            }
            sections.append(section)
        return sections

    # -------------------------------------------------------------------------
    # REAL CONTENT GENERATION
    # -------------------------------------------------------------------------

    def generate_section_content(self, section_id: str, topic: str) -> str:
        """
        Generates real, deterministic content for each section.
        This is the first fully functional content layer.
        """

        topic_clean = topic.strip() if topic else "the lesson topic"

        if section_id == "warmup":
            return (
                f"Let's get started by activating your ideas about **{topic_clean}**.\n\n"
                f"1. When was the last time you travelled anywhere?\n"
                f"2. What kind of trips do you enjoy — relaxing, adventurous, cultural?\n"
                f"3. If you could plan a trip right now, where would you go and why?\n"
                f"4. What makes a trip memorable for you?\n"
            )

        if section_id == "dialogue":
            return (
                f"Here is a short dialogue modelling natural language around **{topic_clean}**.\n\n"
                f"A: I'm thinking about my next trip. Do you have any plans?\n"
                f"B: Actually, yes. I'm planning to visit Spain this summer.\n"
                f"A: Nice! What made you choose Spain?\n"
                f"B: Good weather, great food, and I’ve never been before.\n"
                f"A: Sounds perfect. How long will you stay?\n"
                f"B: About a week. I want to explore a few cities.\n"
            )

        if section_id == "questions":
            return (
                f"Discuss these questions with a partner. They help you explore **{topic_clean}**.\n\n"
                f"1. What destinations are popular in your country?\n"
                f"2. Do you prefer travelling alone or with others? Why?\n"
                f"3. What is the most memorable trip you’ve ever taken?\n"
                f"4. How do you usually plan your trips — spontaneously or carefully?\n"
                f"5. What factors influence your travel decisions (budget, weather, culture)?\n"
            )

        if section_id == "vocab":
            return (
                f"Useful vocabulary for talking about **{topic_clean}**:\n\n"
                f"- **Itinerary** — your plan for