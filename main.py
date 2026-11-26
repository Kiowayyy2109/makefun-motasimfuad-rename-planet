import os

LINE = "I rename this planet Monday - smaller, colder, and nobody wants to go there."

LIMIT = 200
if len(LINE) != 76 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 76 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Rename the planet after the worst day: the joke lands on Monday.
