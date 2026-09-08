import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\di\AppModule.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add AiApi to APIs
if "AiApi::class.java" not in content:
    content = content.replace("single { get<Retrofit>().create(ApplicationApi::class.java) }",
        "single { get<Retrofit>().create(ApplicationApi::class.java) }\n    single { get<Retrofit>().create(AiApi::class.java) }")

# Add AiRepository to Repositories
if "AiRepository(get())" not in content:
    content = content.replace("single { ApplicationRepository(get()) }",
        "single { ApplicationRepository(get()) }\n    single { AiRepository(get()) }")

# Add missing ViewModels
viewmodels_to_add = """
    viewModel { com.lanturn.app.ui.screens.employer.EmployerHomeViewModel(get(), get()) }
    viewModel { com.lanturn.app.ui.screens.employer.EmployerJobsViewModel(get()) }
    viewModel { com.lanturn.app.ui.screens.employer.EmployerProfileViewModel(get()) }
    viewModel { com.lanturn.app.ui.screens.employer.EmployerApplicantsViewModel(get()) }
    viewModel { com.lanturn.app.ui.screens.student.CareerAiViewModel(get()) }
"""
if "EmployerHomeViewModel" not in content:
    content = content.replace("viewModel { com.lanturn.app.ui.screens.student.StudentProfileViewModel(get()) }",
        "viewModel { com.lanturn.app.ui.screens.student.StudentProfileViewModel(get()) }\n" + viewmodels_to_add)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)