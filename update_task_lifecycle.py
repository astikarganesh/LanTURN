import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 1. **Lifecycle & Memory Hardening**", "- `[x]` 1. **Lifecycle & Memory Hardening**")
content = content.replace("- `[ ]` Add `androidx.lifecycle:lifecycle-runtime-compose` dependency.", "- `[x]` Add `androidx.lifecycle:lifecycle-runtime-compose` dependency.")
content = content.replace("- `[ ]` Replace `collectAsState()` with `collectAsStateWithLifecycle()` across all screens.", "- `[x]` Replace `collectAsState()` with `collectAsStateWithLifecycle()` across all screens.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)