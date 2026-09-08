import os
import re

# Update Student
filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentDashboardWrapper.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import androidx.compose.ui.Modifier", "import androidx.compose.ui.Modifier\nimport androidx.compose.material.icons.Icons\nimport androidx.compose.material.icons.filled.*\nimport androidx.compose.material3.Icon")

content = content.replace("icon = { Text(\"H\") }", "icon = { Icon(Icons.Default.Home, contentDescription = \"Home\") }")
content = content.replace("icon = { Text(\"J\") }", "icon = { Icon(Icons.Default.Work, contentDescription = \"Jobs\") }")
content = content.replace("icon = { Text(\"A\") }", "icon = { Icon(Icons.Default.Assignment, contentDescription = \"Apps\") }")
content = content.replace("icon = { Text(\"AI\") }", "icon = { Icon(Icons.Default.SmartToy, contentDescription = \"AI\") }")
content = content.replace("icon = { Text(\"P\") }", "icon = { Icon(Icons.Default.Person, contentDescription = \"Profile\") }")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)


# Update Employer
filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer\EmployerDashboardWrapper.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import androidx.compose.ui.Modifier", "import androidx.compose.ui.Modifier\nimport androidx.compose.material.icons.Icons\nimport androidx.compose.material.icons.filled.*\nimport androidx.compose.material3.Icon")

content = content.replace("icon = { Text(\"H\") }", "icon = { Icon(Icons.Default.Home, contentDescription = \"Home\") }")
content = content.replace("icon = { Text(\"J\") }", "icon = { Icon(Icons.Default.Work, contentDescription = \"Jobs\") }")
content = content.replace("icon = { Text(\"A\") }", "icon = { Icon(Icons.Default.People, contentDescription = \"Applicants\") }")
content = content.replace("icon = { Text(\"C\") }", "icon = { Icon(Icons.Default.Business, contentDescription = \"Company\") }")
content = content.replace("icon = { Text(\"P\") }", "icon = { Icon(Icons.Default.Person, contentDescription = \"Profile\") }")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)