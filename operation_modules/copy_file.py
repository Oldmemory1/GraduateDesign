def copy_file(source_address,destination_address):
    with open(source_address, "rb") as f:
        bytez = f.read()
    with open(destination_address, "wb+") as f1:
        f1.write(bytez)
if __name__ == "__main__":
    copy_file(source_address=r"D:\graduate_design\example1\source_file\sample1.exe",
              destination_address=r"D:\graduate_design\example1\temp\sample1.exe")
