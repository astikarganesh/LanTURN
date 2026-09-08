import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

list_screen = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ApplicantsListScreen(
    viewModel: EmployerApplicantsViewModel = koinViewModel(),
    onApplicantClick: (String) -> Unit
) {
    val state by viewModel.state.collectAsState()

    LaunchedEffect(Unit) {
        viewModel.loadApplications() // Load all for employer
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Applicants") }
            )
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
                if (state.applications.isEmpty()) {
                    item {
                        Text("No applicants yet.")
                    }
                } else {
                    items(state.applications) { application ->
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { onApplicantClick(application.id) }
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text(
                                    text = "Student ID: ${application.studentId}",
                                    style = MaterialTheme.typography.titleMedium,
                                    fontWeight = FontWeight.Bold
                                )
                                Spacer(modifier = Modifier.height(4.dp))
                                Text("Applied for Job ID: ${application.jobId}")
                                Spacer(modifier = Modifier.height(4.dp))
                                
                                val statusColor = when (application.status.name) {
                                    "ACCEPTED" -> MaterialTheme.colorScheme.primary
                                    "REJECTED" -> MaterialTheme.colorScheme.error
                                    else -> MaterialTheme.colorScheme.onSurfaceVariant
                                }
                                Text("Status: ${application.status.name}", color = statusColor)
                            }
                        }
                    }
                }
            }
        }
    }
}
'''

detail_screen = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.ApplicationStatus
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ApplicantDetailScreen(
    applicationId: String,
    viewModel: EmployerApplicantsViewModel = koinViewModel(),
    onBack: () -> Unit
) {
    val state by viewModel.state.collectAsState()
    val application = state.applications.find { it.id == applicationId }

    var showAcceptDialog by remember { mutableStateOf(false) }
    var showRejectDialog by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Application Review") },
                navigationIcon = {
                    TextButton(onClick = onBack) { Text("Back") }
                }
            )
        }
    ) { padding ->
        if (application == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Text("Application not found.")
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                if (state.updateError != null) {
                    Text(text = state.updateError!!, color = MaterialTheme.colorScheme.error)
                }

                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("Application ID: ${application.id}", style = MaterialTheme.typography.titleMedium)
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("Student ID: ${application.studentId}")
                        Text("Job ID: ${application.jobId}")
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("Status: ${application.status.name}")
                        if (!application.employerNotes.isNullOrEmpty()) {
                            Text("Notes: ${application.employerNotes}")
                        }
                    }
                }

                Spacer(modifier = Modifier.weight(1f))

                if (application.status == ApplicationStatus.SUBMITTED || application.status == ApplicationStatus.REVIEWED) {
                    Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                        Button(
                            onClick = { showRejectDialog = true },
                            modifier = Modifier.weight(1f),
                            colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.error)
                        ) {
                            Text("Reject")
                        }
                        Button(
                            onClick = { showAcceptDialog = true },
                            modifier = Modifier.weight(1f)
                        ) {
                            Text("Accept")
                        }
                    }
                }
            }

            if (showAcceptDialog) {
                AlertDialog(
                    onDismissRequest = { showAcceptDialog = false },
                    title = { Text("Accept Applicant?") },
                    text = { Text("Are you sure you want to accept this student for the position?") },
                    confirmButton = {
                        TextButton(onClick = {
                            viewModel.updateApplicationStatus(application.id, ApplicationStatus.ACCEPTED)
                            showAcceptDialog = false
                        }) {
                            Text("Accept")
                        }
                    },
                    dismissButton = {
                        TextButton(onClick = { showAcceptDialog = false }) { Text("Cancel") }
                    }
                )
            }

            if (showRejectDialog) {
                AlertDialog(
                    onDismissRequest = { showRejectDialog = false },
                    title = { Text("Reject Applicant?") },
                    text = { Text("Are you sure you want to reject this application?") },
                    confirmButton = {
                        TextButton(onClick = {
                            viewModel.updateApplicationStatus(application.id, ApplicationStatus.REJECTED)
                            showRejectDialog = false
                        }) {
                            Text("Reject", color = MaterialTheme.colorScheme.error)
                        }
                    },
                    dismissButton = {
                        TextButton(onClick = { showRejectDialog = false }) { Text("Cancel") }
                    }
                )
            }
        }
    }
}
'''

with open(os.path.join(base, "ApplicantsListScreen.kt"), "w", encoding="utf-8") as f:
    f.write(list_screen)
with open(os.path.join(base, "ApplicantDetailScreen.kt"), "w", encoding="utf-8") as f:
    f.write(detail_screen)

print("Applicant screens written")