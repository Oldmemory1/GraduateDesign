import subprocess


def scanner_360sd(input_file_):

    path_360sd = r"C:\Program Files\360\360sd\360sd.exe"
    target_file = input_file_
    subprocess.run(
        [path_360sd,target_file],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )



if __name__ == '__main__':
    scanner_360sd(input_file_=r"D:\graduate_design\example1\sample\6fc3fe100d2e2e8c74ee4d768fb3e3a3ebccd0c5f815c6be4c95fd1a041fda65.exe")
