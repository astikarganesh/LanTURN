import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

jobs_screen = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EmployerJobsScreen(
    viewModel: EmployerJobsViewModel = koinViewModel(),
    onCreateJob: () -> Unit,
    onJobClick: (String) -> Unit
) {
    val state by viewModel.state.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Manage Jobs") }
            )
        },
        floatingActionButton = {
            FloatingActionButton(onClick = onCreateJob) {
                Text("+")
            }
        }
    ) { padding ->
        if (state.isLoading) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else {
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                if (state.jobs.isEmpty()) {
                    item {
                        Text("No jobs posted. Click '+' to create one.")
                    }
                } else {
                    items(state.jobs) { job ->
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { onJobClick(job.id) }
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text(
                                    text = job.title,
                                    style = MaterialTheme.typography.titleLarge,
                                    fontWeight = FontWeight.Bold
                                )
                                Spacer(modifier = Modifier.height(4.dp))
                                Text("Type: ${job.jobType} | Location: ${job.location}")
                                Spacer(modifier = Modifier.height(4.dp))
                                Text("Status: ${job.status}", color = MaterialTheme.colorScheme.primary)
                            }
                        }
                    }
                }
            }
        }
    }
}
'''

create_job = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.JobCreateRequest
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CreateJobScreen(
    viewModel: EmployerJobsViewModel = koinViewModel(),
    onBack: () -> Unit
) {
    val state by viewModel.state.collectAsState()

    var title by remember { mutableStateOf("") }
    var description by remember { mutableStateOf("") }
    var requirements by remember { mutableStateOf("") }
    var jobType by remember { mutableStateOf("FULL_TIME") }
    var location by remember { mutableStateOf("") }
    var industry by remember { mutableStateOf("") }
    var salaryMin by remember { mutableStateOf("") }
    var salaryMax by remember { mutableStateOf("") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Create Job Posting") },
                navigationIcon = {
                    TextButton(onClick = onBack) { Text("Back") }
                }
            )
        }
    ) { padding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            item {
                if (state.saveError != null) {
                    Text(text = state.saveError!!, color = MaterialTheme.colorScheme.error)
                }
            }

            item {
                OutlinedTextField(
                    value = title,
                    onValueChange = { title = it },
                    label = { Text("Job Title") },
                    modifier = Modifier.fillMaxWidth()
                )
            }
            item {
                OutlinedTextField(
                    value = description,
                    onValueChange = { description = it },
                    label = { Text("Description") },
                    modifier = Modifier.fillMaxWidth(),
                    minLines = 3
                )
            }
            item {
                OutlinedTextField(
                    value = requirements,
                    onValueChange = { requirements = it },
                    label = { Text("Requirements (comma separated)") },
                    modifier = Modifier.fillMaxWidth()
                )
            }
            item {
                OutlinedTextField(
                    value = location,
                    onValueChange = { location = it },
                    label = { Text("Location") },
                    modifier = Modifier.fillMaxWidth()
                )
            }
            item {
                OutlinedTextField(
                    value = industry,
                    onValueChange = { industry = it },
                    label = { Text("Industry") },
                    modifier = Modifier.fillMaxWidth()
                )
            }
            item {
                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                    OutlinedTextField(
                        value = salaryMin,
                        onValueChange = { salaryMin = it },
                        label = { Text("Min Salary") },
                        modifier = Modifier.weight(1f)
                    )
                    OutlinedTextField(
                        value = salaryMax,
                        onValueChange = { salaryMax = it },
                        label = { Text("Max Salary") },
                        modifier = Modifier.weight(1f)
                    )
                }
            }
            item {
                Button(
                    onClick = {
                        val reqList = requirements.split(",").map { it.trim() }.filter { it.isNotEmpty() }
                        val request = JobCreateRequest(
                            title = title,
                            description = description,
                            requirements = reqList,
                            jobType = jobType,
                            location = location,
                            industry = industry,
                            salaryMin = salaryMin.toDoubleOrNull(),
                            salaryMax = salaryMax.toDoubleOrNull(),
                            requiredSkills = emptyList() // simplified for now
                        )
                        viewModel.createJob(request) { success ->
                            if (success) onBack()
                        }
                    },
                    modifier = Modifier.fillMaxWidth(),
                    enabled = !state.isSaving && title.isNotBlank() && description.isNotBlank()
                ) {
                    if (state.isSaving) {
                        CircularProgressIndicator(modifier = Modifier.size(24.dp))
                    } else {
                        Text("Post Job")
                    }
                }
            }
        }
    }
}
'''

with open(os.path.join(base, "EmployerJobsScreen.kt"), "w", encoding="utf-8") as f:
    f.write(jobs_screen)
with open(os.path.join(base, "CreateJobScreen.kt"), "w", encoding="utf-8") as f:
    f.write(create_job)

print("Job screens written")