import os
import glob

directory = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".kt"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "import androidx.lifecycle.compose.collectAsStateWithLifecycle\npackage " in content:
                content = content.replace("import androidx.lifecycle.compose.collectAsStateWithLifecycle\npackage ", "package ")
                # Now add it correctly after package
                content = content.replace("package com.lanturn.app.ui.screens", "package com.lanturn.app.ui.screens\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Fixed {file}")
