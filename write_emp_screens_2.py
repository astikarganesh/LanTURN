import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

profile = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
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
fun EmployerProfileScreen(
    viewModel: EmployerProfileViewModel = koinViewModel(),
    onEditProfile: () -> Unit,
    onLogout: () -> Unit
) {
    val state by viewModel.state.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Company Profile") },
                actions = {
                    TextButton(onClick = onEditProfile) {
                        Text("Edit")
                    }
                }
            )
        }
    ) { padding ->
        if (state.isLoading) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(
                            text = state.profile?.companyName ?: "Company Name",
                            style = MaterialTheme.typography.headlineMedium,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(modifier = Modifier.height(8.dp))
                        Text(text = "Location: ${state.profile?.location ?: "Not set"}")
                        Text(text = "Website: ${state.profile?.website ?: "Not set"}")
                        Spacer(modifier = Modifier.height(16.dp))
                        Text(text = "Description:", fontWeight = FontWeight.SemiBold)
                        Text(text = state.profile?.description ?: "No description provided.")
                    }
                }
                
                Spacer(modifier = Modifier.weight(1f))
                
                Button(
                    onClick = onLogout,
                    modifier = Modifier.fillMaxWidth(),
                    colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.error)
                ) {
                    Text("Logout")
                }
            }
        }
    }
}
'''

edit_profile = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.EmployerProfileDto
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EmployerEditProfileScreen(
    viewModel: EmployerProfileViewModel = koinViewModel(),
    onBack: () -> Unit
) {
    val state by viewModel.state.collectAsState()

    var companyName by remember { mutableStateOf(state.profile?.companyName ?: "") }
    var website by remember { mutableStateOf(state.profile?.website ?: "") }
    var location by remember { mutableStateOf(state.profile?.location ?: "") }
    var description by remember { mutableStateOf(state.profile?.description ?: "") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Edit Company Profile") },
                navigationIcon = {
                    TextButton(onClick = onBack) { Text("Back") }
                }
            )
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            if (state.saveError != null) {
                Text(text = state.saveError!!, color = MaterialTheme.colorScheme.error)
            }

            OutlinedTextField(
                value = companyName,
                onValueChange = { companyName = it },
                label = { Text("Company Name") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = website,
                onValueChange = { website = it },
                label = { Text("Website") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = location,
                onValueChange = { location = it },
                label = { Text("Location") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = description,
                onValueChange = { description = it },
                label = { Text("Description") },
                modifier = Modifier.fillMaxWidth(),
                minLines = 4
            )

            Button(
                onClick = {
                    val updatedProfile = EmployerProfileDto(
                        id = state.profile?.id ?: "",
                        userId = state.profile?.userId ?: "",
                        companyName = companyName,
                        website = website,
                        logoUrl = state.profile?.logoUrl,
                        description = description,
                        location = location
                    )
                    viewModel.updateProfile(updatedProfile, onSuccess = onBack)
                },
                modifier = Modifier.fillMaxWidth(),
                enabled = !state.isSaving
            ) {
                if (state.isSaving) {
                    CircularProgressIndicator(modifier = Modifier.size(24.dp))
                } else {
                    Text("Save Changes")
                }
            }
        }
    }
}
'''

with open(os.path.join(base, "EmployerProfileScreen.kt"), "w", encoding="utf-8") as f:
    f.write(profile)
with open(os.path.join(base, "EmployerEditProfileScreen.kt"), "w", encoding="utf-8") as f:
    f.write(edit_profile)

print("Profile screens written")