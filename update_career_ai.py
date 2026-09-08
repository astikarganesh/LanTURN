import os
import re

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\CareerAiScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace hardcoded colors in MessageBubble
content = re.sub(
    r"val backgroundColor = if \(isUser\) Color\(0xFFE3F2FD\) else Color\(0xFFF5F5F5\)\n\s*val textColor = Color\.Black",
    """val backgroundColor = if (isUser) MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surfaceVariant
    val textColor = if (isUser) MaterialTheme.colorScheme.onPrimaryContainer else MaterialTheme.colorScheme.onSurfaceVariant""",
    content
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)