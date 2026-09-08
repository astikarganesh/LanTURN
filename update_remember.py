import os
import re

directory = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".kt"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "remember { mutableStateOf" in content:
                content = content.replace("remember { mutableStateOf", "rememberSaveable { mutableStateOf")
                
                if "import androidx.compose.runtime.saveable.rememberSaveable" not in content:
                    content = content.replace("import androidx.compose.runtime.*", "import androidx.compose.runtime.*\nimport androidx.compose.runtime.saveable.rememberSaveable")
                    
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {file}")
