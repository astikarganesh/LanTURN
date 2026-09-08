import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

edit_profile = '''package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.EmployerProfileDto
import com.lanturn.app.data.models.EmployerLocation
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
    var location by remember { mutableStateOf(state.profile?.location?.city ?: "") }
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
                label = { Text("City") },
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
                        companyName = companyName,
                        website = website,
                        logoURL = state.profile?.logoURL,
                        description = description,
                        location = EmployerLocation(city = location)
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

with open(os.path.join(base, "EmployerEditProfileScreen.kt"), "w", encoding="utf-8") as f:
    f.write(edit_profile)