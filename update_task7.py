import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 7. **Build Verification**", "- `[x]` 7. **Build Verification**")
content = content.replace("- `[ ]` Run `./gradlew assembleDebug`", "- `[x]` Run `./gradlew assembleDebug`")
content = content.replace("- `[ ]` Resolve lint warnings", "- `[x]` Resolve lint warnings")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)