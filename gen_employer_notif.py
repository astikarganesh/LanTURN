import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer\EmployerNotificationsScreen.kt"
content = """package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.background
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
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import org.koin.androidx.compose.koinViewModel
import com.lanturn.app.ui.screens.NotificationViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EmployerNotificationsScreen(
    viewModel: NotificationViewModel = koinViewModel(),
    onNavigateToJobApplicants: (String) -> Unit = {}
) {
    val state by viewModel.state.collectAsState()

    LaunchedEffect(Unit) {
        viewModel.loadNotifications()
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Notifications") },
                actions = {
                    TextButton(onClick = { viewModel.markAllAsRead() }) {
                        Text("Mark all read")
                    }
                }
            )
        }
    ) { padding ->
        if (state.isLoading) {
            Box(Modifier.fillMaxSize().padding(padding), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else if (state.notifications.isEmpty()) {
            Box(Modifier.fillMaxSize().padding(padding), contentAlignment = Alignment.Center) {
                Text("No notifications.")
            }
        } else {
            LazyColumn(modifier = Modifier.padding(padding).fillMaxSize()) {
                items(state.notifications) { notif ->
                    val bgColor = if (!notif.read) MaterialTheme.colorScheme.primaryContainer else Color.Transparent
                    
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(bgColor)
                            .clickable {
                                viewModel.markAsRead(notif.id)
                                // e.g. /employer/jobs/jobId/applicants
                                if (notif.link?.contains("/applicants") == true) {
                                    val parts = notif.link.split("/")
                                    // format: "", "employer", "jobs", "<jobId>", "applicants"
                                    if (parts.size >= 4) {
                                        val jobId = parts[3]
                                        onNavigateToJobApplicants(jobId)
                                    }
                                }
                            }
                            .padding(16.dp)
                    ) {
                        Text(notif.title, fontWeight = if (!notif.read) FontWeight.Bold else FontWeight.Normal)
                        Spacer(modifier = Modifier.height(4.dp))
                        Text(notif.body, style = MaterialTheme.typography.bodyMedium)
                    }
                    Divider()
                }
            }
        }
    }
}
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)