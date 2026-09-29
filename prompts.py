PROMPTS = {
    "explain": """You are a friendly and clear tutor.
Explain the following concept for a {level} learner.
Use simple language, one real-world analogy, and end with a one-line summary.

Concept: {topic}""",

    "notes": """You are an expert note-taker.
Turn the text below into clean, structured study notes.
Use a short title, headings for each main idea, and bullet points under each heading.
Highlight key terms in bold. Keep it concise.

Text:
{text}""",

    "quiz": """You are a quiz creator.
Create {num_questions} multiple-choice questions about the topic below.
Each question must have exactly 4 options and only one correct answer.

Return ONLY valid JSON in this exact format, with no extra text before or after:
[
  {{
    "question": "the question text",
    "options": ["option 1", "option 2", "option 3", "option 4"],
    "answer": "the exact text of the correct option",
    "explanation": "one sentence explaining why it is correct"
  }}
]

Topic or text: {topic}""",
}


def get_prompt(name, **kwargs):
    """Fetch a template by name and fill in its placeholders."""
    return PROMPTS[name].format(**kwargs)


# Quick test: run this file directly to preview the prompts
if __name__ == "__main__":
    print(get_prompt("explain", topic="Recursion", level="beginner"))
    print("-" * 40)
    print(get_prompt("quiz", topic="Photosynthesis", num_questions=3))