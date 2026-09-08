import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 2. **Network Resilience (401 Handling)**", "- `[x]` 2. **Network Resilience (401 Handling)**")
content = content.replace("- `[ ]` Update `AuthInterceptor` (or create global handler) to detect 401.", "- `[x]` Update `AuthInterceptor` (or create global handler) to detect 401.")
content = content.replace("- `[ ]` Implement robust session clearing upon 401.", "- `[x]` Implement robust session clearing upon 401.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)