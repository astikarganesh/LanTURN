import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"

def patch_vm(filename, error_prop="error", loading_prop="isLoading"):
    filepath = os.path.join(base, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple replacement: look for "is ApiResult.Error -> {" block and insert Exception block after it
    # We will just replace "is ApiResult.Error -> {" with the same plus the Exception branch
    
    new_content = ""
    for line in content.split("\n"):
        new_content += line + "\n"
        if "is ApiResult.Error ->" in line:
            indent = line.split("is ")[0]
            # Find the property update inside the block to mimic it? No, just add the exception block right after the error block ends? No, it's easier to replace "when (result) {" with exhaustive blocks.
    
    # A cleaner way is to use regex or just rewrite the whole file. I will rewrite the whole file.