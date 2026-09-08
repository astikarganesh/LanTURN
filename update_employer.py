import sys

file_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer\EmployerEditProfileScreen.kt"

new_code = """package com.lanturn.app.ui.screens.employer

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.EmployerProfileDto
import com.lanturn.app.data.models.EmployerLocation
import com.lanturn.app.data.models.HrContact
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EmployerEditProfileScreen(
    viewModel: EmployerProfileViewModel = koinViewModel(),
    onBack: () -> Unit
) {
    val state by viewModel.state.collectAsStateWithLifecycle()

    var companyName by rememberSaveable { mutableStateOf(state.profile?.companyName ?: "") }
    var website by rememberSaveable { mutableStateOf(state.profile?.website ?: "") }
    var description by rememberSaveable { mutableStateOf(state.profile?.description ?: "") }
    var industry by rememberSaveable { mutableStateOf(state.profile?.industry ?: "") }
    var companySize by rememberSaveable { mutableStateOf(state.profile?.companySize ?: "") }
    var employeeCount by rememberSaveable { mutableStateOf(state.profile?.employeeCount?.toString() ?: "") }
    var foundedYear by rememberSaveable { mutableStateOf(state.profile?.foundedYear?.toString() ?: "") }

    var city by rememberSaveable { mutableStateOf(state.profile?.location?.city ?: "") }
    var stateProvince by rememberSaveable { mutableStateOf(state.profile?.location?.state ?: "") }
    var country by rememberSaveable { mutableStateOf(state.profile?.location?.country ?: "") }
    var headquarters by rememberSaveable { mutableStateOf(state.profile?.headquarters ?: "") }

    var hrName by rememberSaveable { mutableStateOf(state.profile?.hrContact?.name ?: "") }
    var hrEmail by rememberSaveable { mutableStateOf(state.profile?.hrContact?.email ?: "") }
    var hrPhone by rememberSaveable { mutableStateOf(state.profile?.hrContact?.phone ?: "") }
    var ceo by rememberSaveable { mutableStateOf(state.profile?.ceo ?: "") }

    var benefits by rememberSaveable { mutableStateOf(state.profile?.benefits?.joinToString(", ") ?: "") }
    var technologies by rememberSaveable { mutableStateOf(state.profile?.technologies?.joinToString(", ") ?: "") }
    var companyCulture by rememberSaveable { mutableStateOf(state.profile?.companyCulture ?: "") }
    var linkedin by rememberSaveable { mutableStateOf(state.profile?.linkedin ?: "") }
    
    var logoURL by rememberSaveable { mutableStateOf(state.profile?.logoURL ?: "") }

    val snackbarHostState = remember { SnackbarHostState() }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Edit Company Profile") },
                navigationIcon = {
                    TextButton(onClick = onBack) { Text("Back") }
                }
            )
        },
        snackbarHost = { SnackbarHost(snackbarHostState) },
        bottomBar = {
            Surface(tonalElevation = 8.dp, shadowElevation = 8.dp) {
                Box(modifier = Modifier.fillMaxWidth().padding(16.dp)) {
                    Button(
                        onClick = {
                            val updatedProfile = EmployerProfileDto(
                                companyName = companyName.ifBlank { null },
                                website = website.ifBlank { null },
                                description = description.ifBlank { null },
                                industry = industry.ifBlank { null },
                                companySize = companySize.ifBlank { null },
                                employeeCount = employeeCount.toIntOrNull(),
                                foundedYear = foundedYear.toIntOrNull(),
                                location = EmployerLocation(
                                    city = city.ifBlank { null },
                                    state = stateProvince.ifBlank { null },
                                    country = country.ifBlank { null }
                                ),
                                headquarters = headquarters.ifBlank { null },
                                hrContact = HrContact(
                                    name = hrName.ifBlank { null },
                                    email = hrEmail.ifBlank { null },
                                    phone = hrPhone.ifBlank { null }
                                ),
                                ceo = ceo.ifBlank { null },
                                benefits = benefits.split(",").map { it.trim() }.filter { it.isNotEmpty() },
                                technologies = technologies.split(",").map { it.trim() }.filter { it.isNotEmpty() },
                                companyCulture = companyCulture.ifBlank { null },
                                linkedin = linkedin.ifBlank { null },
                                logoURL = logoURL.ifBlank { null }
                            )
                            viewModel.updateProfile(updatedProfile, onSuccess = onBack)
                        },
                        modifier = Modifier.fillMaxWidth(),
                        enabled = !state.isSaving
                    ) {
                        if (state.isSaving) {
                            CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
                        } else {
                            Text("Save Changes")
                        }
                    }
                }
            }
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            if (state.saveError != null) {
                Text(text = state.saveError!!, color = MaterialTheme.colorScheme.error)
            }

            Text("Company Info", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = companyName, onValueChange = { companyName = it }, label = { Text("Company Name") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = description, onValueChange = { description = it }, label = { Text("Description") }, modifier = Modifier.fillMaxWidth(), minLines = 3)
            OutlinedTextField(value = industry, onValueChange = { industry = it }, label = { Text("Industry") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = companySize, onValueChange = { companySize = it }, label = { Text("Company Size") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = employeeCount, onValueChange = { employeeCount = it }, label = { Text("Employee Count") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = foundedYear, onValueChange = { foundedYear = it }, label = { Text("Founded Year") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = website, onValueChange = { website = it }, label = { Text("Website URL") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = logoURL, onValueChange = { logoURL = it }, label = { Text("Logo URL") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = linkedin, onValueChange = { linkedin = it }, label = { Text("LinkedIn URL") }, modifier = Modifier.fillMaxWidth())

            HorizontalDivider()

            Text("Location", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = city, onValueChange = { city = it }, label = { Text("City") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = stateProvince, onValueChange = { stateProvince = it }, label = { Text("State") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = country, onValueChange = { country = it }, label = { Text("Country") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = headquarters, onValueChange = { headquarters = it }, label = { Text("Headquarters") }, modifier = Modifier.fillMaxWidth())

            HorizontalDivider()

            Text("HR & Contact", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = ceo, onValueChange = { ceo = it }, label = { Text("CEO Name") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = hrName, onValueChange = { hrName = it }, label = { Text("HR Name") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = hrEmail, onValueChange = { hrEmail = it }, label = { Text("HR Email") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = hrPhone, onValueChange = { hrPhone = it }, label = { Text("HR Phone") }, modifier = Modifier.fillMaxWidth())

            HorizontalDivider()

            Text("Culture & Tech", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = companyCulture, onValueChange = { companyCulture = it }, label = { Text("Company Culture") }, modifier = Modifier.fillMaxWidth(), minLines = 2)
            OutlinedTextField(value = benefits, onValueChange = { benefits = it }, label = { Text("Benefits (comma-separated)") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = technologies, onValueChange = { technologies = it }, label = { Text("Technologies (comma-separated)") }, modifier = Modifier.fillMaxWidth())
            
            Spacer(modifier = Modifier.height(80.dp))
        }
    }
}
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_code)
print("Updated EmployerEditProfileScreen successfully")
