import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer\EmployerDashboardWrapper.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix import
content = content.replace("import androidx.navigation.toRoute", "import androidx.navigation.toRoute\nimport com.lanturn.app.ui.screens.NotificationViewModel\nimport org.koin.androidx.compose.koinViewModel")

# Fix navigation in composable
content = content.replace("EmployerNotificationsScreen()", """EmployerNotificationsScreen(
                    onNavigateToJobApplicants = { navController.navigate(EmployerApplicantsRoute) }
                )""")

# Add BadgedBox in EmployerBottomBar
content = content.replace("fun EmployerBottomBar(navController: NavController) {", """fun EmployerBottomBar(navController: NavController, notifViewModel: NotificationViewModel = koinViewModel()) {
    val notifState by notifViewModel.state.collectAsState()
""")

content = content.replace("""            NavigationBarItem(
                icon = { Text("N") },
                label = { Text("Notif") },""", """            NavigationBarItem(
                icon = { 
                    BadgedBox(
                        badge = {
                            if (notifState.unreadCount > 0) {
                                Badge { Text(notifState.unreadCount.toString()) }
                            }
                        }
                    ) {
                        Text("N") 
                    }
                },
                label = { Text("Notifs") },""")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)