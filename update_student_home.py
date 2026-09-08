import os
import re

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentHomeScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# I will replace the Box(Modifier.fillMaxSize()) with LanTURN components.
content = content.replace("import org.koin.androidx.compose.koinViewModel", "import org.koin.androidx.compose.koinViewModel\nimport com.lanturn.app.ui.components.*")

# Replace standard loading and error blocks
content = re.sub(
    r"if \(state.isLoading && state.profile == null\) \{.*?\}\s*else if \(state.error != null && state.profile == null\) \{.*?\} else \{",
    """if (state.isLoading && state.profile == null) {
            LanTURNLoadingOverlay()
        } else if (state.error != null && state.profile == null) {
            LanTURNErrorState(message = state.error ?: "Failed to load dashboard", onRetry = { viewModel.loadDashboardData() })
        } else {""",
    content,
    flags=re.DOTALL
)

# Replace the inner Scaffold padding to be applied correctly to the scroll column
content = content.replace("modifier = Modifier.padding(padding).fillMaxSize().verticalScroll(rememberScrollState()).padding(16.dp)", 
                          "modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(padding).padding(16.dp)")

# Standardize cards
content = content.replace("Card(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp))", 
                          "Card(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant), elevation = CardDefaults.cardElevation(defaultElevation = 2.dp))")

content = content.replace("Card(modifier = Modifier.width(280.dp).padding(end = 16.dp))", 
                          "Card(modifier = Modifier.width(280.dp).padding(end = 16.dp), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant), elevation = CardDefaults.cardElevation(defaultElevation = 2.dp))")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)