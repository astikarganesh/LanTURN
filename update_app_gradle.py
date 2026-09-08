import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\build.gradle.kts"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add dependencies
if "libs.googleid" not in content:
    deps = """
    implementation(libs.androidx.credentials)
    implementation(libs.androidx.credentials.play.services.auth)
    implementation(libs.googleid)
"""
    content = content.replace("dependencies {", "dependencies {" + deps)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)