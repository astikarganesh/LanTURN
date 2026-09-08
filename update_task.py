import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 1. **Core Design System**", "- `[x]` 1. **Core Design System**")
content = content.replace("- `[ ]` Update `Color.kt`", "- `[x]` Update `Color.kt`")
content = content.replace("- `[ ]` Update `Theme.kt`", "- `[x]` Update `Theme.kt`")
content = content.replace("- `[ ]` Update `Type.kt`", "- `[x]` Update `Type.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)