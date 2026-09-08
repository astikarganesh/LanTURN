import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 4. **UI Edge Cases (Rotation & Keyboard)**", "- `[x]` 4. **UI Edge Cases (Rotation & Keyboard)**")
content = content.replace("- `[ ]` Audit text fields for `rememberSaveable` to protect against rotation.", "- `[x]` Audit text fields for `rememberSaveable` to protect against rotation.")
content = content.replace("- `[ ]` Ensure scrolling behavior is smooth when keyboard appears.", "- `[x]` Ensure scrolling behavior is smooth when keyboard appears.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)