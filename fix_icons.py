import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\CareerAiScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Remove imports
content = content.replace("import androidx.compose.material.icons.Icons", "")
content = content.replace("import androidx.compose.material.icons.filled.Send", "")

# Replace Icon with Text
content = content.replace('Icon(Icons.Default.Send, contentDescription = "Send message")', 'Text("Send")')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)