import os
import re

def fix_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\student"

fix_file(os.path.join(base, "StudentHomeScreen.kt"), [
    ('text = "Welcome, $"{"{state.profile?.personal?.name ?: "Student"}",', 'text = "Welcome, ${state.profile?.personal?.name ?: \\"Student\\"}",')
])

fix_file(os.path.join(base, "StudentProfileScreen.kt"), [
    ('Text("${"{profile.personal.city ?: ""}", "${"{profile.personal.state ?: ""}",', 'Text("${profile.personal.city ?: \\"\\"}, ${profile.personal.state ?: \\"\\"}",'),
    ('Text("${"{profile.academic.degree ?: ""} ${"{profile.academic.branch ?: ""}",', 'Text("${profile.academic.degree ?: \\"\\"} ${profile.academic.branch ?: \\"\\"}",'),
    ('Text("Graduation: $"{"{profile.academic.graduationYear ?: "N/A"}"} | CGPA: $"{"{profile.academic.cgpa ?: "N/A"}"}",', 'Text("Graduation: ${profile.academic.graduationYear ?: \\"N/A\\"} | CGPA: ${profile.academic.cgpa ?: \\"N/A\\"}",'),
    ('Text("`${`"{profile.personal.city ?: `"`"}", `"`$"{`"{profile.personal.state ?: `"`"}",', 'Text("${profile.personal.city ?: \\"\\"}, ${profile.personal.state ?: \\"\\"}",'),
    ('Text("`${`"{profile.academic.degree ?: `"`"} `"`$"{`"{profile.academic.branch ?: `"`"}",', 'Text("${profile.academic.degree ?: \\"\\"} ${profile.academic.branch ?: \\"\\"}",')
])

fix_file(os.path.join(base, "ApplicationsListScreen.kt"), [
    ('Text("Application ID: $"{"{app.id.take(8)}..."}",', 'Text("Application ID: ${app.id.take(8)}...",'),
    ('Text("Job ID: $"{"{app.jobId}"}",', 'Text("Job ID: ${app.jobId}",')
])

fix_file(os.path.join(base, "JobsListScreen.kt"), [
    ('Text("• $"req",', 'Text("• ${req}",')
])

# Use regex to just fix everything blindly just in case the exact string match fails
def regex_fix(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # fix $"{"{var}"}
    content = re.sub(r'\$""?\{"\{([^}]+)\}"\}', r'${\1}', content)
    # fix ${"{var}"}
    content = re.sub(r'\$\{""?\{([^}]+)\}""?\}', r'${\1}', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

regex_fix(os.path.join(base, "StudentHomeScreen.kt"))
regex_fix(os.path.join(base, "StudentProfileScreen.kt"))
regex_fix(os.path.join(base, "ApplicationsListScreen.kt"))
regex_fix(os.path.join(base, "JobsListScreen.kt"))
