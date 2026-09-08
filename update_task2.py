import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 2. **Reusable UI Components**", "- `[x]` 2. **Reusable UI Components**")
content = content.replace("- `[ ]` Create `Buttons.kt`", "- `[x]` Create `Buttons.kt`")
content = content.replace("- `[ ]` Create `Inputs.kt`", "- `[x]` Create `Inputs.kt`")
content = content.replace("- `[ ]` Create `States.kt`", "- `[x]` Create `States.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)