import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\gradle\libs.versions.toml"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

if "koinVersion" not in content:
    content = content.replace("[versions]", "[versions]\nkoinVersion = \"3.5.3\"")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)