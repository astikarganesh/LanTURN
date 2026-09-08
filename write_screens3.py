import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student"

home = '''package com.lanturn.app.ui.screens.student

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun StudentHomeScreen(
    viewModel: StudentHomeViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Dashboard") },
                actions = {
                    Button(onClick = { viewModel.loadDashboardData() }) {
                        Text("Refresh")
                    }
                }
            )
        }
    ) { padding ->
        if (state.isLoading && state.profile == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else if (state.error != null && state.profile == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(text = state.error ?: "Error", color = MaterialTheme.colorScheme.error)
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = { viewModel.loadDashboardData() }) {
                        Text("Retry")
                    }
                }
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .verticalScroll(rememberScrollState())
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(24.dp)
            ) {
                Text(
                    text = "Welcome, ${state.profile?.personal?.name ?: "Student"}",
                    style = MaterialTheme.typography.headlineMedium,
                    fontWeight = FontWeight.Bold
                )

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    StatCard(
                        modifier = Modifier.weight(1f),
                        title = "Profile",
                        value = "80%"
                    )
                    StatCard(
                        modifier = Modifier.weight(1f),
                        title = "Applications",
                        value = "3"
                    )
                }

                Text(
                    text = "Recommended Jobs",
                    style = MaterialTheme.typography.titleLarge,
                    fontWeight = FontWeight.SemiBold
                )
                
                if (state.recommendedJobs.isEmpty()) {
                    Card(
                        modifier = Modifier.fillMaxWidth(),
                        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant)
                    ) {
                        Box(
                            modifier = Modifier.fillMaxWidth().padding(32.dp),
                            contentAlignment = Alignment.Center
                        ) {
                            Text("No jobs found matching your profile.", color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    }
                } else {
                    LazyRow(
                        horizontalArrangement = Arrangement.spacedBy(16.dp),
                        contentPadding = PaddingValues(end = 16.dp)
                    ) {
                        items(state.recommendedJobs) { job ->
                            Card(
                                modifier = Modifier.width(280.dp),
                                onClick = { /* Navigate to detail */ }
                            ) {
                                Column(modifier = Modifier.padding(16.dp)) {
                                    Text(job.title, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold, maxLines = 1)
                                    Spacer(modifier = Modifier.height(8.dp))
                                    Text(job.description, style = MaterialTheme.typography.bodyMedium, maxLines = 2)
                                    Spacer(modifier = Modifier.height(16.dp))
                                    Text(job.jobType.name, style = MaterialTheme.typography.labelSmall, color = MaterialTheme.colorScheme.secondary)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun StatCard(modifier: Modifier = Modifier, title: String, value: String) {
    Card(modifier = modifier) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(value, style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
            Text(title, style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}'''

profile = '''package com.lanturn.app.ui.screens.student

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.lanturn.app.data.models.StudentProfileDto
import com.lanturn.app.domain.LogoutUseCase
import kotlinx.coroutines.launch
import org.koin.androidx.compose.koinViewModel
import org.koin.compose.koinInject

@OptIn(ExperimentalLayoutApi::class, ExperimentalMaterial3Api::class)
@Composable
fun StudentProfileScreen(
    onEditProfile: () -> Unit,
    onLogout: () -> Unit,
    viewModel: StudentProfileViewModel = koinViewModel(),
    logoutUseCase: LogoutUseCase = koinInject()
) {
    val state by viewModel.state.collectAsState()
    val scope = rememberCoroutineScope()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Profile") },
                actions = {
                    Button(onClick = onEditProfile) {
                        Text("Edit")
                    }
                    Button(onClick = {
                        scope.launch {
                            logoutUseCase()
                            onLogout()
                        }
                    }) {
                        Text("Logout")
                    }
                }
            )
        }
    ) { padding ->
        if (state.isLoading && state.profile == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else if (state.error != null && state.profile == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(text = state.error ?: "Error", color = MaterialTheme.colorScheme.error)
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = { viewModel.loadProfile() }) {
                        Text("Retry")
                    }
                }
            }
        } else {
            val profile = state.profile
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .verticalScroll(rememberScrollState())
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(
                        modifier = Modifier.padding(24.dp).fillMaxWidth(),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(profile?.personal?.name ?: "Student Name", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
                        if (profile?.personal?.city != null || profile?.personal?.state != null) {
                            Text("${profile.personal.city ?: ""}, ${profile.personal.state ?: ""}", style = MaterialTheme.typography.bodyMedium)
                        }
                    }
                }

                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("Education", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
                        Spacer(modifier = Modifier.height(8.dp))
                        if (profile?.academic != null) {
                            Text(profile.academic.college ?: "No college specified", style = MaterialTheme.typography.bodyLarge)
                            Text("${profile.academic.degree ?: ""} ${profile.academic.branch ?: ""}", style = MaterialTheme.typography.bodyMedium)
                            Text("Graduation: ${profile.academic.graduationYear ?: "N/A"} | CGPA: ${profile.academic.cgpa ?: "N/A"}", style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        } else {
                            Text("No education details added.", color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    }
                }

                Card(modifier = Modifier.fillMaxWidth()) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text("Skills", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
                        Spacer(modifier = Modifier.height(8.dp))
                        val skills = profile?.professional?.skills ?: emptyList()
                        if (skills.isNotEmpty()) {
                            FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                                skills.forEach { skill ->
                                    SuggestionChip(onClick = {}, label = { Text(skill) })
                                }
                            }
                        } else {
                            Text("No skills added.", color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                    }
                }
                Spacer(modifier = Modifier.height(80.dp))
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun EditProfileScreen(
    onBack: () -> Unit,
    viewModel: StudentProfileViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsState()
    var name by remember { mutableStateOf(state.profile?.personal?.name ?: "") }
    var city by remember { mutableStateOf(state.profile?.personal?.city ?: "") }
    var college by remember { mutableStateOf(state.profile?.academic?.college ?: "") }
    
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
                                    city = city.ifBlank { null }
                                ),
                                academic = (currentProfile.academic ?: com.lanturn.app.data.models.AcademicInfo()).copy(
                                    college = college.ifBlank { null }
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
            OutlinedTextField(
                value = name,
                onValueChange = { name = it },
                label = { Text("Full Name") },
                modifier = Modifier.fillMaxWidth()
            )
            OutlinedTextField(
                value = city,
                onValueChange = { city = it },
                label = { Text("City") },
                modifier = Modifier.fillMaxWidth()
            )
            
            HorizontalDivider()
            
            Text("Academic Information", style = MaterialTheme.typography.titleLarge)
            OutlinedTextField(
                value = college,
                onValueChange = { college = it },
                label = { Text("College/University") },
                modifier = Modifier.fillMaxWidth()
            )
            Spacer(modifier = Modifier.height(80.dp))
        }
    }
}'''

jobs = '''package com.lanturn.app.ui.screens.student

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import org.koin.androidx.compose.koinViewModel
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun JobsListScreen(
    viewModel: JobsViewModel = koinViewModel(),
    onJobClick: (String) -> Unit
) {
    val state by viewModel.state.collectAsState()
    var searchQuery by remember { mutableStateOf(state.searchQuery) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Jobs") }
            )
        }
    ) { padding ->
        Column(modifier = Modifier.padding(padding).fillMaxSize()) {
            OutlinedTextField(
                value = searchQuery,
                onValueChange = { searchQuery = it },
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                placeholder = { Text("Search jobs...") },
                singleLine = true
            )

            if (state.isLoading) {
                Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                    CircularProgressIndicator()
                }
            } else if (state.error != null) {
                Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                    Text(text = state.error ?: "Error", color = MaterialTheme.colorScheme.error)
                }
            } else if (state.jobs.isEmpty()) {
                Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                    Text("No jobs found.", color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
            } else {
                LazyColumn(
                    contentPadding = PaddingValues(16.dp),
                    verticalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    items(state.jobs) { job ->
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { onJobClick(job.id) }
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text(job.title, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                                Spacer(modifier = Modifier.height(8.dp))
                                Text(job.description, style = MaterialTheme.typography.bodyMedium, maxLines = 3)
                                Spacer(modifier = Modifier.height(16.dp))
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween
                                ) {
                                    SuggestionChip(
                                        onClick = { },
                                        label = { Text(job.jobType.name) }
                                    )
                                    if (job.location != null) {
                                        Text(job.location.city ?: "Remote", style = MaterialTheme.typography.labelMedium)
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun JobDetailScreen(
    jobId: String,
    onBack: () -> Unit,
    viewModel: JobsViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsState()
    val job = state.jobs.find { it.id == jobId }
    val scope = rememberCoroutineScope()
    val snackbarHostState = remember { SnackbarHostState() }
    var isApplying by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Job Details") },
                navigationIcon = {
                    Button(onClick = onBack) {
                        Text("Back")
                    }
                }
            )
        },
        snackbarHost = { SnackbarHost(snackbarHostState) },
        bottomBar = {
            if (job != null) {
                Surface(
                    tonalElevation = 8.dp,
                    shadowElevation = 8.dp
                ) {
                    Box(modifier = Modifier.fillMaxWidth().padding(16.dp)) {
                        Button(
                            onClick = {
                                isApplying = true
                                viewModel.applyForJob(job.id) { success, msg ->
                                    isApplying = false
                                    scope.launch {
                                        if (success) {
                                            snackbarHostState.showSnackbar("Application submitted successfully!")
                                        } else {
                                            snackbarHostState.showSnackbar(msg ?: "Failed to apply")
                                        }
                                    }
                                }
                            },
                            modifier = Modifier.fillMaxWidth(),
                            enabled = !isApplying
                        ) {
                            if (isApplying) {
                                CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
                            } else {
                                Text("Apply Now")
                            }
                        }
                    }
                }
            }
        }
    ) { padding ->
        if (job == null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Text("Job not found")
            }
        } else {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(padding)
                    .verticalScroll(rememberScrollState())
                    .padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                Text(job.title, style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
                
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    AssistChip(onClick = {}, label = { Text(job.jobType.name) })
                    if (job.workMode != null) {
                        AssistChip(onClick = {}, label = { Text(job.workMode.name) })
                    }
                }
                
                HorizontalDivider()
                
                Text("Description", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                Text(job.description, style = MaterialTheme.typography.bodyMedium)
                
                if (job.requirements.isNotEmpty()) {
                    Text("Requirements", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                    job.requirements.forEach { req ->
                        Text("• ${req}", style = MaterialTheme.typography.bodyMedium)
                    }
                }
                
                if (job.requiredSkills.isNotEmpty()) {
                    Text("Skills", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        job.requiredSkills.forEach { skill ->
                            SuggestionChip(onClick = {}, label = { Text(skill) })
                        }
                    }
                }
                Spacer(modifier = Modifier.height(80.dp))
            }
        }
    }
}'''

apps = '''package com.lanturn.app.ui.screens.student

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
fun ApplicationsListScreen(
    viewModel: ApplicationsViewModel = koinViewModel()
) {
    val state by viewModel.state.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("My Applications") },
                actions = {
                    Button(onClick = { viewModel.loadApplications() }) {
                        Text("Refresh")
                    }
                }
            )
        }
    ) { padding ->
        if (state.isLoading) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        } else if (state.error != null) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(text = state.error ?: "Error", color = MaterialTheme.colorScheme.error)
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(onClick = { viewModel.loadApplications() }) {
                        Text("Retry")
                    }
                }
            }
        } else if (state.applications.isEmpty()) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Text("You haven't applied to any jobs yet.", color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        } else {
            LazyColumn(
                contentPadding = PaddingValues(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier.padding(padding).fillMaxSize()
            ) {
                items(state.applications) { app ->
                    Card(modifier = Modifier.fillMaxWidth()) {
                        Column(modifier = Modifier.padding(16.dp)) {
                            Text("Application ID: ${app.id.take(8)}...", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                            Spacer(modifier = Modifier.height(8.dp))
                            Text("Job ID: ${app.jobId}", style = MaterialTheme.typography.bodyMedium)
                            Spacer(modifier = Modifier.height(16.dp))
                            
                            val statusColor = when(app.status.name) {
                                "SUBMITTED" -> MaterialTheme.colorScheme.primary
                                "REVIEWED" -> MaterialTheme.colorScheme.secondary
                                "ACCEPTED" -> androidx.compose.ui.graphics.Color(0xFF4CAF50)
                                "REJECTED" -> MaterialTheme.colorScheme.error
                                else -> MaterialTheme.colorScheme.onSurfaceVariant
                            }
                            
                            SuggestionChip(
                                onClick = { },
                                label = { Text(app.status.name, color = statusColor) }
                            )
                        }
                    }
                }
            }
        }
    }
}'''

nav = '''package com.lanturn.app.ui.screens.student

import androidx.compose.foundation.layout.padding
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.navigation.NavController
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import androidx.navigation.toRoute

@Composable
fun StudentDashboardWrapper(onLogout: () -> Unit) {
    val navController = rememberNavController()
    
    Scaffold(
        bottomBar = { StudentBottomBar(navController) }
    ) { innerPadding ->
        NavHost(
            navController = navController,
            startDestination = StudentHomeRoute,
            modifier = Modifier.padding(innerPadding)
        ) {
            composable<StudentHomeRoute> {
                StudentHomeScreen()
            }
            composable<StudentJobsRoute> {
                JobsListScreen(
                    onJobClick = { jobId -> navController.navigate(StudentJobDetailRoute(jobId)) }
                )
            }
            composable<StudentJobDetailRoute> { backStackEntry ->
                val route = backStackEntry.toRoute<StudentJobDetailRoute>()
                JobDetailScreen(jobId = route.jobId, onBack = { navController.popBackStack() })
            }
            composable<StudentApplicationsRoute> {
                ApplicationsListScreen()
            }
            composable<StudentCareerAiRoute> {
                CareerAiScreen()
            }
            composable<StudentProfileRoute> {
                StudentProfileScreen(
                    onEditProfile = { navController.navigate(StudentEditProfileRoute) },
                    onLogout = onLogout
                )
            }
            composable<StudentEditProfileRoute> {
                EditProfileScreen(onBack = { navController.popBackStack() })
            }
        }
    }
}

@Composable
fun StudentBottomBar(navController: NavController) {
    val navBackStackEntry by navController.currentBackStackEntryAsState()
    val currentDestination = navBackStackEntry?.destination

    val showBottomBar = currentDestination?.hierarchy?.any { 
        it.route?.contains("StudentHomeRoute") == true ||
        it.route?.contains("StudentJobsRoute") == true ||
        it.route?.contains("StudentApplicationsRoute") == true ||
        it.route?.contains("StudentCareerAiRoute") == true ||
        it.route?.contains("StudentProfileRoute") == true 
    } == true && 
    currentDestination.hierarchy.none {
        it.route?.contains("StudentJobDetailRoute") == true ||
        it.route?.contains("StudentEditProfileRoute") == true
    }

    if (showBottomBar) {
        NavigationBar {
            NavigationBarItem(
                icon = { Text("H") },
                label = { Text("Home") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentHomeRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentHomeRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("J") },
                label = { Text("Jobs") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentJobsRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentJobsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("A") },
                label = { Text("Apps") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentApplicationsRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentApplicationsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("AI") },
                label = { Text("AI") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentCareerAiRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentCareerAiRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("P") },
                label = { Text("Profile") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentProfileRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentProfileRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
        }
    }
}'''

with open(os.path.join(base, "StudentHomeScreen.kt"), "w", encoding="utf-8") as f:
    f.write(home)
with open(os.path.join(base, "StudentProfileScreen.kt"), "w", encoding="utf-8") as f:
    f.write(profile)
with open(os.path.join(base, "JobsListScreen.kt"), "w", encoding="utf-8") as f:
    f.write(jobs)
with open(os.path.join(base, "ApplicationsListScreen.kt"), "w", encoding="utf-8") as f:
    f.write(apps)
with open(os.path.join(base, "StudentDashboardWrapper.kt"), "w", encoding="utf-8") as f:
    f.write(nav)
