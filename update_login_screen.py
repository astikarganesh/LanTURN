import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\LoginScreen.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

imports = """
import androidx.credentials.CredentialManager
import androidx.credentials.GetCredentialRequest
import androidx.credentials.exceptions.GetCredentialException
import androidx.credentials.CustomCredential
import com.google.android.libraries.identity.googleid.GetGoogleIdOption
import com.google.android.libraries.identity.googleid.GoogleIdTokenCredential
import kotlinx.coroutines.launch
import androidx.compose.ui.platform.LocalContext
"""

if "import androidx.credentials.CredentialManager" not in content:
    content = content.replace("import androidx.compose.runtime.rememberCoroutineScope", "import androidx.compose.runtime.rememberCoroutineScope\n" + imports)

# Find the Composable function definition and add the coroutine scope and context
if "val context = LocalContext.current" not in content:
    content = content.replace("val password = rememberSaveable { mutableStateOf(\"\") }", "val password = rememberSaveable { mutableStateOf(\"\") }\n    val context = LocalContext.current\n    val coroutineScope = rememberCoroutineScope()")

# Replace the TODO button with actual implementation
todo_btn = """              LanTURNSecondaryButton(
                  text = "Login with Google",
                  onClick = { /* TODO: Proper Google Sign In */ }
              )"""

actual_btn = """              LanTURNSecondaryButton(
                  text = "Login with Google",
                  onClick = {
                      coroutineScope.launch {
                          val credentialManager = CredentialManager.create(context)
                          val googleIdOption = GetGoogleIdOption.Builder()
                              .setFilterByAuthorizedAccounts(false)
                              .setServerClientId("842440970364-3icclmhn3c0v6pas11fsesqc70sq8a3o.apps.googleusercontent.com")
                              .setAutoSelectEnabled(false)
                              .build()
                              
                          val request = GetCredentialRequest.Builder()
                              .addCredentialOption(googleIdOption)
                              .build()
                              
                          try {
                              val result = credentialManager.getCredential(context, request)
                              val credential = result.credential
                              
                              if (credential is CustomCredential && credential.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                                  val googleIdTokenCredential = GoogleIdTokenCredential.createFrom(credential.data)
                                  viewModel.loginWithGoogle(googleIdTokenCredential.idToken)
                              }
                          } catch (e: GetCredentialException) {
                              // Handle failure (e.g., user dismissed the dialog)
                          }
                      }
                  }
              )"""

content = content.replace(todo_btn, actual_btn)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)