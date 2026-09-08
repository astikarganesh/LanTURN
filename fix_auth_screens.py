import os
import re

login_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\LoginScreen.kt"
with open(login_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("if (state.isAuthenticated)", "if (state is AuthState.Success)")
content = content.replace("state.isAuthenticated", "state is AuthState.Success")
content = content.replace("state.isLoading", "state is AuthState.Loading")
content = content.replace("state.error != null", "state is AuthState.Error")
content = content.replace("state.error ?: \"\"", "(state as? AuthState.Error)?.message ?: \"\"")
content = content.replace("viewModel.loginWithGoogle()", "viewModel.signInWithGoogle(android.credentials.GetCredentialResponse(android.os.Bundle())) // TODO: Proper Google Sign In")

with open(login_path, "w", encoding="utf-8") as f:
    f.write(content)


register_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\RegisterScreen.kt"
with open(register_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("if (state.isAuthenticated)", "if (state is AuthState.Success)")
content = content.replace("state.isAuthenticated", "state is AuthState.Success")
content = content.replace("state.isLoading", "state is AuthState.Loading")
content = content.replace("state.error != null", "state is AuthState.Error")
content = content.replace("state.error ?: \"\"", "(state as? AuthState.Error)?.message ?: \"\"")

with open(register_path, "w", encoding="utf-8") as f:
    f.write(content)