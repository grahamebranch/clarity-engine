# test_simple_engine.py
from rameon_core.engine.simple_engine import SimpleEngine


engine = SimpleEngine()

result = engine.run("""
Heading One
This is a paragraph.

Heading Two
- Bullet A
- Bullet B
""")

print(result)
print("\n=== SECOND TEST ===\n")

text2 = """
## Overview
This is a short intro.

## Details
- Item one
- Item two

A final paragraph that should merge cleanly.
"""

result2 = engine.run(text2)
print(result2)
print("\n=== THIRD TEST ===\n")

text3 = """
Title
A paragraph with some text.

Another paragraph after a blank line.

1. First item
2. Second item

"""

result3 = engine.run(text3)
print(result3)
print("\n=== FINAL CONFIRMATION TEST ===\n")

text4 = """
# Alpha
- One
- Two

A paragraph after bullets.

# Beta
- Three
- Four
"""

result4 = engine.run(text4)
print(result4)
