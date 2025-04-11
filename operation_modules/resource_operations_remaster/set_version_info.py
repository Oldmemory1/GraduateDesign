import random
import string
import subprocess


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def set_version_info(input_file):
    rcedit_path = "rcedit-x64.exe"
    FileDescription = generate_random_string(50)
    CompanyName = generate_random_string(50)
    LegalCopyright = generate_random_string(50)
    ProductName = generate_random_string(50)
    file_version = "0.0.1"
    FileVersion = "0.0.1"
    product_version = "0.0.1"

    command = [
        rcedit_path,
        input_file,
        "--set-version-string", "FileDescription", FileDescription,
        "--set-version-string", "CompanyName", CompanyName,
        "--set-version-string", "LegalCopyright", LegalCopyright,
        "--set-version-string", "ProductName", ProductName,
        "--set-file-version", file_version,
        "--set-version-string", "FileVersion", FileVersion,
        "--set-product-version", product_version
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if __name__ == "__main__":
    set_version_info(r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\test_sample\sample1.exe")