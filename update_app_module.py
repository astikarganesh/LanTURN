import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\di\AppModule.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("single { get<Retrofit>().create(AiApi::class.java) }", "single { get<Retrofit>().create(AiApi::class.java) }\n    single { get<Retrofit>().create(NotificationApi::class.java) }")
content = content.replace("single { AiRepository(get()) }", "single { AiRepository(get()) }\n    single { NotificationRepository(get()) }")
content = content.replace("viewModel { com.lanturn.app.ui.screens.student.CareerAiViewModel(get()) }", "viewModel { com.lanturn.app.ui.screens.student.CareerAiViewModel(get()) }\n    viewModel { com.lanturn.app.ui.screens.NotificationViewModel(get()) }")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)