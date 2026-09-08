import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentRoutes.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content += "\n@Serializable\nobject StudentNotificationsRoute\n"

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)