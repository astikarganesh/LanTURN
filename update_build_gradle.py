import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\build.gradle.kts"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("implementation(libs.androidx.compose.material3)", "implementation(libs.androidx.compose.material3)\n    implementation(\"androidx.compose.material:material-icons-extended\")")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)