import os

login_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\LoginScreen.kt"
with open(login_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("onLoginSuccess: () -> Unit", "onLoginSuccess: (String) -> Unit")
content = content.replace("onLoginSuccess()", "onLoginSuccess((state as AuthState.Success).role.name)")

with open(login_path, "w", encoding="utf-8") as f:
    f.write(content)

reg_path = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\RegisterScreen.kt"
with open(reg_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("onRegisterSuccess: () -> Unit", "onRegisterSuccess: (String) -> Unit")
content = content.replace("onRegisterSuccess()", "onRegisterSuccess((state as AuthState.Success).role.name)")

with open(reg_path, "w", encoding="utf-8") as f:
    f.write(content)