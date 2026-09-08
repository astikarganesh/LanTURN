import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 4. **Student Experience Refinement**", "- `[x]` 4. **Student Experience Refinement**")
content = content.replace("- `[ ]` Update `StudentHomeScreen.kt`", "- `[x]` Update `StudentHomeScreen.kt`")
content = content.replace("- `[ ]` Update `JobsListScreen.kt`", "- `[x]` Update `JobsListScreen.kt`")
content = content.replace("- `[ ]` Update `ApplicationsListScreen.kt`", "- `[x]` Update `ApplicationsListScreen.kt`")
content = content.replace("- `[ ]` Update `CareerAiScreen.kt`", "- `[x]` Update `CareerAiScreen.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)