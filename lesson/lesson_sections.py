"""
Lesson Sections — deterministic content generator aligned with the upgraded engine.
Supports all section IDs defined in LessonArchitectureBuilder.
"""

from typing import List, Dict


class LessonSectionsBuilder:
    """
    Builds concrete lesson sections from the architecture.
    Deterministic, topic-aware, extensible.
    """

    def build_sections(self, architecture: List[Dict[str, str]], topic: str) -> List[Dict[str, str]]:
        sections = []
        for spec in architecture:
            section_id = spec["id"]
            title = spec["title"]
            content = self.generate_section_content(section_id, topic)
            sections.append({
                "id": section_id,
                "title": title,
                "content": content,
            })
        return sections

    # ---------------------------------------------------------
    # CONTENT GENERATION
    # ---------------------------------------------------------

    def generate_section_content(self, section_id: str, topic: str) -> str:
        """
        Deterministic content for each section ID.
        Supports all architectures: conversation, vocabulary, grammar.
        """

        topic_clean = topic.strip() if topic else "the lesson topic"

        # -------------------------
        # Conversation Architecture
        # -------------------------

        if section_id == "warmup":
            return (
                f"Let's activate your ideas about **{topic_clean}**.\n\n"
                f"1. What comes to mind when you think about this topic?\n"
                f"2. Have you talked about this before? With whom?\n"
                f"3. Why do you think this topic matters in everyday life?\n"
            )

        if section_id == "dialogue":
            return (
                f"Here is a short dialogue modelling natural language around **{topic_clean}**.\n\n"
                f"A: I've been thinking about {topic_clean} lately.\n"
                f"B: Really? What made you think about it?\n"
                f"A: I saw something online and it caught my attention.\n"
                f"B: Interesting. What do you find most important about it?\n"
            )

        if section_id == "questions":
            return (
                f"Discuss these questions to explore **{topic_clean}** more deeply:\n\n"
                f"1. What do people usually think about this topic?\n"
                f"2. How does it affect your daily life?\n"
                f"3. What experiences have shaped your views on it?\n"
                f"4. What challenges or opportunities does it create?\n"
            )

        if section_id == "vocab":
            return (
                f"Useful vocabulary for talking about **{topic_clean}**:\n\n"
                f"- **Key concept** — an important idea related to the topic.\n"
                f"- **Example** — a situation that illustrates the idea.\n"
                f"- **Perspective** — a way of looking at the topic.\n"
                f"- **Impact** — how the topic influences people or situations.\n"
                f"- **Context** — the background or situation in which the topic appears.\n"
            )

        if section_id == "practice":
            return (
                f"Practise using language connected to **{topic_clean}**:\n\n"
                f"1. Describe a situation where this topic was important.\n"
                f"2. Explain your opinion about it.\n"
                f"3. Role‑play a short conversation about it.\n"
                f"4. Give advice to someone dealing with an issue related to it.\n"
            )

        if section_id == "reflection":
            return (
                f"Reflect on **{topic_clean}**:\n\n"
                f"- What did you learn today?\n"
                f"- Did any ideas surprise you?\n"
                f"- How confident do you feel discussing this topic now?\n"
                f"- What would you like to explore further?\n"
            )

        # -------------------------
        # Vocabulary Architecture
        # -------------------------

        if section_id == "input":
            return (
                f"Read this short text introducing vocabulary related to **{topic_clean}**:\n\n"
                f"People often encounter {topic_clean} in different situations. "
                f"Understanding the key terms helps you communicate clearly and confidently.\n"
            )

        if section_id == "items":
            return (
                f"Target vocabulary for **{topic_clean}**:\n\n"
                f"- **Term 1** — definition and example.\n"
                f"- **Term 2** — definition and example.\n"
                f"- **Term 3** — definition and example.\n"
                f"- **Term 4** — definition and example.\n"
            )

        if section_id == "free":
            return (
                f"Use the new vocabulary related to **{topic_clean}** in open‑ended tasks:\n\n"
                f"- Describe a personal experience.\n"
                f"- Give advice using the new terms.\n"
                f"- Create a short story or scenario.\n"
            )

        # -------------------------
        # Grammar Architecture
        # -------------------------

        if section_id == "context":
            return (
                f"Here is a natural example of grammar related to **{topic_clean}**:\n\n"
                f"\"When people talk about {topic_clean}, they often use this structure...\"\n"
            )

        if section_id == "noticing":
            return (
                f"Notice how the grammar works in the context of **{topic_clean}**:\n\n"
                f"- What forms do you see?\n"
                f"- What meaning do they express?\n"
                f"- How does the structure change in different situations?\n"
            )

        if section_id == "clarification":
            return (
                f"Clarification of the grammar point related to **{topic_clean}**:\n\n"
                f"- Form: how the structure is built.\n"
                f"- Meaning: what it expresses.\n"
                f"- Use: when and why speakers choose it.\n"
            )

        if section_id == "production":
            return (
                f"Use the grammar related to **{topic_clean}** in freer tasks:\n\n"
                f"- Describe a situation using the structure.\n"
                f"- Give advice or opinions.\n"
                f"- Create a short dialogue.\n"
            )

        # -------------------------
        # Fallback
        # -------------------------

        return (
            f"This section is not fully defined yet, but it relates to **{topic_clean}**.\n"
            f"Your teacher can use this space for custom tasks or notes.\n"
        )
