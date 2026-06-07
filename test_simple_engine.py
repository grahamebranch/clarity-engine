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
