import os
import time
# upx加壳处理 直接作用于目标文件
# completed
def upx_encryption(input_file):
    # upx加壳直接处理目标文件 处理后的文件位于目标路径
    log1 = "D:\\毕业设计\\example1\\logs\\%s-%s-%s" % (
    "UPX_Process",os.path.basename(input_file), time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()))
    log1 = log1 + ".log"
    command = "D:\\毕业设计\\example1\\upx_shell\\upx.exe %s > %s" %(input_file,log1)
    os.system(command)
    #os.remove(log1)

if __name__ == "__main__":
    upx_encryption(r"D:\毕业设计\example1\source_file\sample1.exe")