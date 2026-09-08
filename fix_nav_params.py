import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\navigation\Navigation.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("onBack = { navController.popBackStack() },", "onNavigateToLogin = { navController.popBackStack() },")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)