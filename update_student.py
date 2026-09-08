import sys

file_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentProfileScreen.kt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of EditProfileScreen
start_marker = "@OptIn(ExperimentalMaterial3Api::class)\n@Composable\nfun EditProfileScreen("
start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find EditProfileScreen")
    sys.exit(1)

new_code = """@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EditProfileScreen(
    onBack: () -> Unit,
    viewModel: StudentProfileViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    var name by rememberSaveable { mutableStateOf(state.profile?.personal?.name ?: "") }
    var phone by rememberSaveable { mutableStateOf(state.profile?.personal?.phone ?: "") }
    var city by rememberSaveable { mutableStateOf(state.profile?.personal?.city ?: "") }
    var stateProvince by rememberSaveable { mutableStateOf(state.profile?.personal?.state ?: "") }
    var country by rememberSaveable { mutableStateOf(state.profile?.personal?.country ?: "") }
    
    var college by rememberSaveable { mutableStateOf(state.profile?.academic?.college ?: "") }
    var degree by rememberSaveable { mutableStateOf(state.profile?.academic?.degree ?: "") }
    var branch by rememberSaveable { mutableStateOf(state.profile?.academic?.branch ?: "") }
    var graduationYear by rememberSaveable { mutableStateOf(state.profile?.academic?.graduationYear?.toString() ?: "") }
    var cgpa by rememberSaveable { mutableStateOf(state.profile?.academic?.cgpa?.toString() ?: "") }
    
    var skills by rememberSaveable { mutableStateOf(state.profile?.professional?.skills?.joinToString(", ") ?: "") }
    var resumeUrl by rememberSaveable { mutableStateOf(state.profile?.professional?.resumeUrl ?: "") }
    
    var github by rememberSaveable { mutableStateOf(state.profile?.social?.github ?: "") }
    var linkedin by rememberSaveable { mutableStateOf(state.profile?.social?.linkedin ?: "") }
    var portfolio by rememberSaveable { mutableStateOf(state.profile?.social?.portfolio ?: "") }

    val scope = rememberCoroutineScope()
    val snackbarHostState = remember { SnackbarHostState() }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Edit Profile") },
                navigationIcon = {
                    Button(onClick = onBack) {
                        Text("Back")
                    }
                }
            )
        },
        snackbarHost = { SnackbarHost(snackbarHostState) },
        bottomBar = {
            Surface(tonalElevation = 8.dp, shadowElevation = 8.dp) {
                Box(modifier = Modifier.fillMaxWidth().padding(16.dp)) {
                    Button(
                        onClick = {
                            val currentProfile = state.profile ?: StudentProfileDto()
                            val updatedProfile = currentProfile.copy(
                                personal = (currentProfile.personal ?: com.lanturn.app.data.models.PersonalInfo()).copy(
                                    name = name.ifBlank { null },
                                    phone = phone.ifBlank { null },
                                    city = city.ifBlank { null },
                                    state = stateProvince.ifBlank { null },
                                    country = country.ifBlank { null }
                                ),
                                academic = (currentProfile.academic ?: com.lanturn.app.data.models.AcademicInfo()).copy(
                                    college = college.ifBlank { null },
                                    degree = degree.ifBlank { null },
                                    branch = branch.ifBlank { null },
                                    graduationYear = graduationYear.toIntOrNull(),
                                    cgpa = cgpa.toDoubleOrNull()
                                ),
                                professional = (currentProfile.professional ?: com.lanturn.app.data.models.ProfessionalInfo()).copy(
                                    skills = skills.split(",").map { it.trim() }.filter { it.isNotEmpty() },
                                    resumeUrl = resumeUrl.ifBlank { null }
                                ),
                                social = (currentProfile.social ?: com.lanturn.app.data.models.SocialInfo()).copy(
                                    github = github.ifBlank { null },
                                    linkedin = linkedin.ifBlank { null },
                                    portfolio = portfolio.ifBlank { null }
                                )
                            )
                            viewModel.updateProfile(updatedProfile) {
                                scope.launch {
                                    snackbarHostState.showSnackbar("Profile updated successfully")
                                    onBack()
                                }
                            }
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
            
            Text("Personal Information", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = name, onValueChange = { name = it }, label = { Text("Full Name") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = phone, onValueChange = { phone = it }, label = { Text("Phone") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = city, onValueChange = { city = it }, label = { Text("City") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = stateProvince, onValueChange = { stateProvince = it }, label = { Text("State") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = country, onValueChange = { country = it }, label = { Text("Country") }, modifier = Modifier.fillMaxWidth())
            
            HorizontalDivider()
            
            Text("Academic Information", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = college, onValueChange = { college = it }, label = { Text("College/University") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = degree, onValueChange = { degree = it }, label = { Text("Degree (e.g. B.Tech)") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = branch, onValueChange = { branch = it }, label = { Text("Branch") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = graduationYear, onValueChange = { graduationYear = it }, label = { Text("Graduation Year") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = cgpa, onValueChange = { cgpa = it }, label = { Text("CGPA") }, modifier = Modifier.fillMaxWidth())

            HorizontalDivider()
            
            Text("Professional Information", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = skills, onValueChange = { skills = it }, label = { Text("Skills (comma-separated)") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = resumeUrl, onValueChange = { resumeUrl = it }, label = { Text("Resume Link (URL)") }, modifier = Modifier.fillMaxWidth())
            
            HorizontalDivider()
            
            Text("Social Links", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(value = github, onValueChange = { github = it }, label = { Text("GitHub Profile URL") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = linkedin, onValueChange = { linkedin = it }, label = { Text("LinkedIn Profile URL") }, modifier = Modifier.fillMaxWidth())
            OutlinedTextField(value = portfolio, onValueChange = { portfolio = it }, label = { Text("Portfolio URL") }, modifier = Modifier.fillMaxWidth())

            Spacer(modifier = Modifier.height(80.dp))
        }
    }
}
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content[:start_idx] + new_code)
print("Updated successfully")
