import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 3. **Auth Flow UX Refinement**", "- `[x]` 3. **Auth Flow UX Refinement**")
content = content.replace("- `[ ]` Update `LoginScreen.kt`", "- `[x]` Update `LoginScreen.kt`")
content = content.replace("- `[ ]` Update `RegisterScreen.kt`", "- `[x]` Update `RegisterScreen.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)