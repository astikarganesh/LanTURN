import os
import glob
import re

directory = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".kt"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find and fix the incorrect package/import replacements
            if "import androidx.lifecycle.compose.collectAsStateWithLifecycle.student" in content:
                content = content.replace(
                    "package com.lanturn.app.ui.screens\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle.student",
                    "package com.lanturn.app.ui.screens.student\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle"
                )
                
            if "import androidx.lifecycle.compose.collectAsStateWithLifecycle.employer" in content:
                content = content.replace(
                    "package com.lanturn.app.ui.screens\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle.employer",
                    "package com.lanturn.app.ui.screens.employer\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle"
                )
                
            if "import androidx.lifecycle.compose.collectAsStateWithLifecycle.auth" in content:
                content = content.replace(
                    "package com.lanturn.app.ui.screens\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle.auth",
                    "package com.lanturn.app.ui.screens.auth\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle"
                )
                
            if "import androidx.lifecycle.compose.collectAsStateWithLifecycle.dashboard" in content:
                content = content.replace(
                    "package com.lanturn.app.ui.screens\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle.dashboard",
                    "package com.lanturn.app.ui.screens.dashboard\n\nimport androidx.lifecycle.compose.collectAsStateWithLifecycle"
                )
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            