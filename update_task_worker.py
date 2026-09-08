import os

filepath = r"C:\Users\Aravind\.gemini\antigravity-ide\brain\d8e90e3a-a2ac-4540-bcd3-7122d9030885\task.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("- `[ ]` 3. **Background Notifications (WorkManager)**", "- `[x]` 3. **Background Notifications (WorkManager)**")
content = content.replace("- `[ ]` Add `androidx.work:work-runtime-ktx` dependency.", "- `[x]` Add `androidx.work:work-runtime-ktx` dependency.")
content = content.replace("- `[ ]` Create `NotificationWorker` to poll backend.", "- `[x]` Create `NotificationWorker` to poll backend.")
content = content.replace("- `[ ]` Schedule worker on app startup/login.", "- `[x]` Schedule worker on app startup/login.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)