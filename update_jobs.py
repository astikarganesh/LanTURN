import os
import re

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\JobsListScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import org.koin.androidx.compose.koinViewModel", "import org.koin.androidx.compose.koinViewModel\nimport com.lanturn.app.ui.components.*")
content = content.replace("import androidx.compose.ui.text.font.FontWeight\nimport androidx.compose.ui.unit.dp", "import androidx.compose.ui.text.font.FontWeight\nimport androidx.compose.ui.unit.dp\nimport androidx.compose.foundation.text.KeyboardOptions\nimport androidx.compose.foundation.text.KeyboardActions\nimport androidx.compose.ui.text.input.ImeAction")

# Replace Search Bar
content = re.sub(
    r"OutlinedTextField\(\s*value = searchQuery,\s*onValueChange = \{ searchQuery = it \},\s*modifier = Modifier\s*\.fillMaxWidth\(\)\s*\.padding\(16\.dp\),\s*label = \{ Text\(\"Search jobs...\"\) \}\s*\)",
    """LanTURNTextField(
                value = searchQuery,
                onValueChange = { searchQuery = it },
                modifier = Modifier.padding(16.dp),
                label = "Search jobs...",
                keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
                keyboardActions = KeyboardActions(onSearch = { viewModel.setSearchQuery(searchQuery) })
            )""",
    content
)

content = content.replace("Button(onClick = { viewModel.setSearchQuery(searchQuery) }, modifier = Modifier.padding(horizontal = 16.dp)) {",
                          "LanTURNPrimaryButton(onClick = { viewModel.setSearchQuery(searchQuery) }, text = \"Search\", modifier = Modifier.padding(horizontal = 16.dp)) //")

# Standardize Card
content = content.replace("Card(modifier = Modifier.fillMaxWidth().padding(8.dp).clickable { onJobClick(job.id) })",
                          "Card(modifier = Modifier.fillMaxWidth().padding(8.dp).clickable { onJobClick(job.id) }, colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant), elevation = CardDefaults.cardElevation(defaultElevation = 2.dp))")

# Empty State
content = re.sub(
    r"if \(state.jobs\.isEmpty\(\)\) \{\s*item \{\s*Text\(\"No jobs found\", modifier = Modifier.padding\(16.dp\)\)\s*\}\s*\}",
    """if (state.jobs.isEmpty()) {
                        item { LanTURNEmptyState(message = "No jobs found") }
                    }""",
    content
)

content = re.sub(
    r"if \(state.isLoading\) \{\s*Box\(modifier = Modifier.fillMaxSize\(\), contentAlignment = Alignment.Center\) \{\s*CircularProgressIndicator\(\)\s*\}\s*\} else if \(state.error != null\) \{\s*Box\(modifier = Modifier.fillMaxSize\(\), contentAlignment = Alignment.Center\) \{\s*Text\(state.error \?: \"\", color = MaterialTheme.colorScheme.error\)\s*\}\s*\} else \{",
    """if (state.isLoading) {
                LanTURNLoadingOverlay()
            } else if (state.error != null) {
                LanTURNErrorState(message = state.error ?: "Error loading jobs", onRetry = { viewModel.loadJobs() })
            } else {""",
    content
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)