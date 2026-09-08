import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

# Fix ApplicantDetailScreen
detail_file = os.path.join(base, "ApplicantDetailScreen.kt")
with open(detail_file, "r", encoding="utf-8") as f:
    detail_content = f.read()

# Replace references to employerNotes
detail_content = detail_content.replace("application.employerNotes", "application.notes")
# Replace .isNullOrEmpty().not() if any, or !application.notes.isNullOrEmpty()
# Let's just do a safe replace for line 59 and 60
lines = detail_content.split("\n")
new_lines = []
for line in lines:
    if "if (!application.employerNotes.isNullOrEmpty()) {" in line:
        new_lines.append(line.replace("if (!application.employerNotes.isNullOrEmpty()) {", "if (!application.notes.isNullOrEmpty()) {"))
    elif "if (!application.notes.isNullOrEmpty()) {" in line:
        new_lines.append(line.replace("if (!application.notes.isNullOrEmpty()) {", "if (application.notes != null && application.notes.isNotEmpty()) {"))
    else:
        new_lines.append(line)
        
with open(detail_file, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines).replace("application.notes.isNullOrEmpty()", "application.notes?.isEmpty() == true"))

# Fix CreateJobScreen
create_job_file = os.path.join(base, "CreateJobScreen.kt")
with open(create_job_file, "r", encoding="utf-8") as f:
    create_content = f.read()

# We need to add imports for JobType, JobLocation, Salary
if "import com.lanturn.app.data.models.JobType" not in create_content:
    create_content = create_content.replace("import com.lanturn.app.data.models.JobCreateRequest", 
        "import com.lanturn.app.data.models.JobCreateRequest\nimport com.lanturn.app.data.models.JobType\nimport com.lanturn.app.data.models.JobLocation\nimport com.lanturn.app.data.models.Salary")

# Replace jobType = jobType
create_content = create_content.replace("jobType = jobType,", "jobType = JobType.FULL_TIME,")
create_content = create_content.replace("location = location,", "location = JobLocation(city = location),")
create_content = create_content.replace("salaryMin = salaryMin.toDoubleOrNull(),", "salary = Salary(min = salaryMin.toDoubleOrNull(), max = salaryMax.toDoubleOrNull()),")
create_content = create_content.replace("salaryMax = salaryMax.toDoubleOrNull(),", "")

with open(create_job_file, "w", encoding="utf-8") as f:
    f.write(create_content)