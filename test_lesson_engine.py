import sys, os

# Add the parent directory of this file (the project root) to sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

import json
from lesson.lesson_generator import LessonGenerator

def main():
    generator = LessonGenerator()

    payload = {
        "mode": "lesson",
        "text": "Let's practise talking about travel plans. I want a student_plus edition."
    }

    result = generator.run(payload)

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
