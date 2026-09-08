import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentDashboardWrapper.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the NavigationBarItem for Notifications if needed, or add one.
# First add the Route
content = content.replace("import androidx.navigation.toRoute", "import androidx.navigation.toRoute\nimport com.lanturn.app.ui.screens.NotificationViewModel\nimport org.koin.androidx.compose.koinViewModel")

# Add the composable
composable_code = """            composable<StudentProfileRoute> {
                StudentProfileScreen(
                    onEditProfile = { navController.navigate(StudentEditProfileRoute) },
                    onLogout = onLogout
                )
            }
            composable<StudentNotificationsRoute> {
                StudentNotificationsScreen(
                    onNavigateToJob = { jobId -> navController.navigate(StudentJobDetailRoute(jobId)) },
                    onNavigateToApplication = { navController.navigate(StudentApplicationsRoute) }
                )
            }"""

content = content.replace("""            composable<StudentProfileRoute> {
                StudentProfileScreen(
                    onEditProfile = { navController.navigate(StudentEditProfileRoute) },
                    onLogout = onLogout
                )
            }""", composable_code)

# Add to bottom bar show logic
content = content.replace("it.route?.contains(\"StudentProfileRoute\") == true", "it.route?.contains(\"StudentProfileRoute\") == true ||\n        it.route?.contains(\"StudentNotificationsRoute\") == true")

# Add Nav item
nav_item_code = """            NavigationBarItem(
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
            NavigationBarItem(
                icon = { Text("N") },
                label = { Text("Notifs") },
                selected = currentDestination?.hierarchy?.any { it.route?.contains("StudentNotificationsRoute") == true } == true,
                onClick = {
                    navController.navigate(StudentNotificationsRoute) {
                        popUpTo(navController.graph.findStartDestination().id) { saveState = true }
                        launchSingleTop = true
                        restoreState = true
                    }
                }
            )"""

content = content.replace("""            NavigationBarItem(
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
            )""", nav_item_code)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)