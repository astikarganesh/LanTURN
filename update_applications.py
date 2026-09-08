import os
import re

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\ApplicationsListScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import org.koin.androidx.compose.koinViewModel", "import org.koin.androidx.compose.koinViewModel\nimport com.lanturn.app.ui.components.*")

content = content.replace("Card(modifier = Modifier.fillMaxWidth().padding(8.dp))",
                          "Card(modifier = Modifier.fillMaxWidth().padding(8.dp), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant), elevation = CardDefaults.cardElevation(defaultElevation = 2.dp))")

content = re.sub(
    r"if \(state.applications\.isEmpty\(\)\) \{\s*item \{\s*Text\(\"No applications found\", modifier = Modifier.padding\(16.dp\)\)\s*\}\s*\}",
    """if (state.applications.isEmpty()) {
                        item { LanTURNEmptyState(message = "No applications found") }
                    }""",
    content
)

content = re.sub(
    r"if \(state.isLoading\) \{\s*Box\(modifier = Modifier.fillMaxSize\(\), contentAlignment = Alignment.Center\) \{\s*CircularProgressIndicator\(\)\s*\}\s*\} else if \(state.error != null\) \{\s*Box\(modifier = Modifier.fillMaxSize\(\), contentAlignment = Alignment.Center\) \{\s*Text\(state.error \?: \"\", color = MaterialTheme.colorScheme.error\)\s*\}\s*\} else \{",
    """if (state.isLoading) {
                LanTURNLoadingOverlay()
            } else if (state.error != null) {
                LanTURNErrorState(message = state.error ?: "Error loading applications", onRetry = { viewModel.loadApplications() })
            } else {""",
    content
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)