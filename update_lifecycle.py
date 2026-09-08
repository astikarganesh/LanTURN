import os
import glob

directory = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".kt"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if ".collectAsState(" in content:
                # Add import if missing
                if "import androidx.lifecycle.compose.collectAsStateWithLifecycle" not in content:
                    content = content.replace("import androidx.compose.runtime.*", "import androidx.compose.runtime.*\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle")
                    if "import androidx.lifecycle.compose.collectAsStateWithLifecycle" not in content:
                        content = content.replace("import androidx.compose.runtime.collectAsState", "import androidx.lifecycle.compose.collectAsStateWithLifecycle")
                    if "import androidx.lifecycle.compose.collectAsStateWithLifecycle" not in content:
                        # Find package line and insert after it
                        content = content.replace("package ", "import androidx.lifecycle.compose.collectAsStateWithLifecycle\npackage ")

                # Replace usage
                content = content.replace(".collectAsState()", ".collectAsStateWithLifecycle()")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {file}")
