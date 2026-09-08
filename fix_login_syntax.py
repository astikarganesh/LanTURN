import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\LoginScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("onClick = { viewModel.signInWithGoogle(android.credentials.GetCredentialResponse(android.os.Bundle())) // TODO: Proper Google Sign In }",
                          "onClick = { /* TODO: Proper Google Sign In */ }")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)