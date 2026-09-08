import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\auth\AuthViewModel.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add imports
if "import com.google.firebase.auth.GoogleAuthProvider" not in content:
    content = content.replace("import com.google.firebase.auth.FirebaseAuth", "import com.google.firebase.auth.FirebaseAuth\nimport com.google.firebase.auth.GoogleAuthProvider")

# Add loginWithGoogle method
if "fun loginWithGoogle(" not in content:
    login_google_code = """
    fun loginWithGoogle(idToken: String) {
        viewModelScope.launch {
            _authState.value = AuthState.Loading
            try {
                val credential = GoogleAuthProvider.getCredential(idToken, null)
                firebaseAuth.signInWithCredential(credential).await()
                
                val sessionResult = getSessionUseCase()
                if (sessionResult.isSuccess) {
                    val role = sessionResult.getOrNull()?.second ?: Role.UNKNOWN
                    _authState.value = AuthState.Success(role)
                } else {
                    _authState.value = AuthState.Error(sessionResult.exceptionOrNull()?.message ?: "Backend sync failed")
                }
            } catch (e: Exception) {
                _authState.value = AuthState.Error(e.message ?: "Google Login failed")
            }
        }
    }
"""
    content = content.replace("    fun register(email: String, pass: String) {", login_google_code + "\n    fun register(email: String, pass: String) {")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)