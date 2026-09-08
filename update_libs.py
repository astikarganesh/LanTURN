import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\gradle\libs.versions.toml"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add googleid version
if "googleid = " not in content:
    content = content.replace('credentials = "1.3.0"', 'credentials = "1.3.0"\ngoogleid = "1.1.1"')

# Add googleid library
if "googleid = {" not in content:
    content = content.replace('androidx-credentials-play-services-auth = { module = "androidx.credentials:credentials-play-services-auth", version.ref = "credentials" }', 'androidx-credentials-play-services-auth = { module = "androidx.credentials:credentials-play-services-auth", version.ref = "credentials" }\ngoogleid = { module = "com.google.android.libraries.identity.googleid:googleid", version.ref = "googleid" }')

# In case the replace failed due to multiline string match issue, let's just append if not found
if "googleid = {" not in content:
    content = content.replace("[libraries]", "[libraries]\ngoogleid = { module = \"com.google.android.libraries.identity.googleid:googleid\", version.ref = \"googleid\" }")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)