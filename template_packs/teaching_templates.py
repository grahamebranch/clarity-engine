"""
Teaching Templates Pack - v1.0

Provides content templates for each OSF section.
These are NOT final text — they are patterns Rameon fills.
"""

def get_teaching_templates():
    return {
        "version": "TPL-TEACHING-1",

        "warmup": [
            "Start with a simple question: {question}",
            "Ask the learner to describe: {prompt}",
            "Use a quick icebreaker: {activity}"
        ],

        "presentation": [
            "Introduce the topic with a short explanation: {context}",
            "Model the target language: {example}",
            "Provide a simple rule or pattern: {rule}"
        ],

        "controlled_practice": [
            "Give a guided prompt: {prompt}",
            "Ask the learner to complete: {exercise}",
            "Provide a substitution drill: {drill}"
        ],

        "freer_practice": [
            "Encourage open speaking: {scenario}",
            "Ask the learner to share a personal story: {story_prompt}",
            "Use a role-play setup: {roleplay}"
        ],

        "reflection": [
            "Ask the learner what felt easy or difficult: {reflection_q}",
            "Prompt them to notice new vocabulary: {vocab_prompt}",
            "Encourage self-assessment: {self_check}"
        ],

        "assessment": [
            "Check understanding with a quick question: {check_q}",
            "Ask the learner to produce the target form: {target_task}",
            "Give a short comprehension check: {mini_test}"
        ],

        "homework": [
            "Assign a short writing task: {writing_task}",
            "Suggest a speaking practice activity: {speaking_task}",
            "Recommend a vocabulary review: {vocab_review}"
        ]
    }
