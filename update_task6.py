import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 6. **Global Navigation & Responsiveness**", "- `[x]` 6. **Global Navigation & Responsiveness**")
content = content.replace("- `[ ]` Update `StudentDashboardWrapper.kt` & `EmployerDashboardWrapper.kt`", "- `[x]` Update `StudentDashboardWrapper.kt` & `EmployerDashboardWrapper.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)