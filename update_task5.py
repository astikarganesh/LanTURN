import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 5. **Employer Experience Refinement**", "- `[x]` 5. **Employer Experience Refinement**")
content = content.replace("- `[ ]` Update `EmployerHomeScreen.kt`", "- `[x]` Update `EmployerHomeScreen.kt`")
content = content.replace("- `[ ]` Update `CreateJobScreen.kt`", "- `[x]` Update `CreateJobScreen.kt`")
content = content.replace("- `[ ]` Update `ApplicantsListScreen.kt`", "- `[x]` Update `ApplicantsListScreen.kt`")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)