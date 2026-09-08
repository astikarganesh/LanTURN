import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student\StudentDashboardWrapper.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add BadgedBox in StudentBottomBar
content = content.replace("fun StudentBottomBar(navController: NavController) {", """fun StudentBottomBar(navController: NavController, notifViewModel: NotificationViewModel = koinViewModel()) {
    val notifState by notifViewModel.state.collectAsState()
""")

content = content.replace("""            NavigationBarItem(
                icon = { Text("N") },
                label = { Text("Notifs") },""", """            NavigationBarItem(
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