import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\navigation\Navigation.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

import_statement = """import androidx.compose.runtime.LaunchedEffect
import com.lanturn.app.data.network.AuthEvent
import com.lanturn.app.data.network.AuthEventBus
"""

if "com.lanturn.app.data.network.AuthEventBus" not in content:
    content = content.replace("import androidx.compose.runtime.Composable", import_statement + "import androidx.compose.runtime.Composable")

effect_code = """    val navController = rememberNavController()

    LaunchedEffect(Unit) {
        AuthEventBus.events.collect { event ->
            when (event) {
                is AuthEvent.Unauthorized -> {
                    navController.navigate(Routes.LOGIN) {
                        popUpTo(0) { inclusive = true }
                    }
                }
            }
        }
    }
"""

content = content.replace("    val navController = rememberNavController()", effect_code)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)