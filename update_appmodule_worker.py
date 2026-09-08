import os

filepath = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\di\AppModule.kt"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

import_statement = "import org.koin.androidx.workmanager.dsl.worker\n"

if "org.koin.androidx.workmanager.dsl.worker" not in content:
    content = content.replace("import org.koin.dsl.module", import_statement + "import org.koin.dsl.module")

worker_declaration = "\n    // Workers\n    worker { com.lanturn.app.workers.NotificationWorker(get(), get()) }\n"

if "NotificationWorker" not in content:
    content = content.replace("viewModel { com.lanturn.app.ui.screens.NotificationViewModel(get()) }", "viewModel { com.lanturn.app.ui.screens.NotificationViewModel(get()) }" + worker_declaration)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)