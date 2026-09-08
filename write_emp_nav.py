import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"
os.makedirs(base, exist_ok=True)

routes = '''package com.lanturn.app.ui.screens.employer

import kotlinx.serialization.Serializable

@Serializable
object EmployerHomeRoute

@Serializable
object EmployerCompanyRoute

@Serializable
object EmployerEditCompanyRoute

@Serializable
object EmployerJobsRoute

@Serializable
object EmployerCreateJobRoute

@Serializable
data class EmployerJobDetailRoute(val jobId: String)

@Serializable
object EmployerApplicantsRoute

@Serializable
data class EmployerApplicantDetailRoute(val applicationId: String)

@Serializable
object EmployerNotificationsRoute
'''

wrapper = '''package com.lanturn.app.ui.screens.employer

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
fun EmployerDashboardWrapper(onLogout: () -> Unit) {
    val navController = rememberNavController()
    
    Scaffold(
        bottomBar = { EmployerBottomBar(navController) }
    ) { innerPadding ->
        NavHost(
            navController = navController,
            startDestination = EmployerHomeRoute,
            modifier = Modifier.padding(innerPadding)
        ) {
            composable<EmployerHomeRoute> {
                EmployerHomeScreen()
            }
            composable<EmployerCompanyRoute> {
                EmployerProfileScreen(
                    onEditProfile = { navController.navigate(EmployerEditCompanyRoute) },
                    onLogout = onLogout
                )
            }
            composable<EmployerEditCompanyRoute> {
                EmployerEditProfileScreen(onBack = { navController.popBackStack() })
            }
            composable<EmployerJobsRoute> {
                EmployerJobsScreen(
                    onCreateJob = { navController.navigate(EmployerCreateJobRoute) },
                    onJobClick = { jobId -> navController.navigate(EmployerJobDetailRoute(jobId)) }
                )
            }
            composable<EmployerCreateJobRoute> {
                CreateJobScreen(onBack = { navController.popBackStack() })
            }
            composable<EmployerJobDetailRoute> { backStackEntry ->
                // Basic stub or logic for job detail (employers view)
                val route = backStackEntry.toRoute<EmployerJobDetailRoute>()
                // We'll reuse EmployerJobsScreen view or a specific JobDetailScreen for employer if we write one.
                // For now, let's just use a simple placeholder or navigate back.
            }
            composable<EmployerApplicantsRoute> {
                ApplicantsListScreen(
                    onApplicantClick = { appId -> navController.navigate(EmployerApplicantDetailRoute(appId)) }
                )
            }
            composable<EmployerApplicantDetailRoute> { backStackEntry ->
                val route = backStackEntry.toRoute<EmployerApplicantDetailRoute>()
                ApplicantDetailScreen(
                    applicationId = route.applicationId,
                    onBack = { navController.popBackStack() }
                )
            }
            composable<EmployerNotificationsRoute> {
                EmployerNotificationsScreen()
            }
        }
    }
}

@Composable
fun EmployerBottomBar(navController: NavController) {
    val navBackStackEntry by navController.currentBackStackEntryAsState()
    val currentDestination = navBackStackEntry?.destination

    val showBottomBar = currentDestination?.hierarchy?.any { 
        it.route?.contains("EmployerHomeRoute") == true ||
        it.route?.contains("EmployerCompanyRoute") == true ||
        it.route?.contains("EmployerJobsRoute") == true ||
        it.route?.contains("EmployerApplicantsRoute") == true ||
        it.route?.contains("EmployerNotificationsRoute") == true
    } == true && 
    currentDestination.hierarchy.none {
        it.route?.contains("EmployerEditCompanyRoute") == true ||
        it.route?.contains("EmployerCreateJobRoute") == true ||
        it.route?.contains("EmployerApplicantDetailRoute") == true ||
        it.route?.contains("EmployerJobDetailRoute") == true
    }

    if (showBottomBar) {
        NavigationBar {
            NavigationBarItem(
                icon = { Text("H") },
                label = { Text("Home") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("EmployerHomeRoute") == true } == true,
                onClick = {
                    navController.navigate(EmployerHomeRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("J") },
                label = { Text("Jobs") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("EmployerJobsRoute") == true } == true,
                onClick = {
                    navController.navigate(EmployerJobsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("A") },
                label = { Text("Apps") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("EmployerApplicantsRoute") == true } == true,
                onClick = {
                    navController.navigate(EmployerApplicantsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("N") },
                label = { Text("Notif") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("EmployerNotificationsRoute") == true } == true,
                onClick = {
                    navController.navigate(EmployerNotificationsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
            NavigationBarItem(
                icon = { Text("C") },
                label = { Text("Company") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("EmployerCompanyRoute") == true } == true,
                onClick = {
                    navController.navigate(EmployerCompanyRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )
        }
    }
}
'''

with open(os.path.join(base, "EmployerRoutes.kt"), "w", encoding="utf-8") as f:
    f.write(routes)
with open(os.path.join(base, "EmployerDashboardWrapper.kt"), "w", encoding="utf-8") as f:
    f.write(wrapper)

print("Navigation and Routes generated")