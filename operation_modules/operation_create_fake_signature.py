import os
import random
import time


from init.reset_test_enviroment import init_environment
from operation_modules.copy_file import copy_file
from operation_modules.findAllSignatures import get_all_file_paths


# completed
# 添加伪造的签名 但是最后会复制一个文件回来
def create_fake_signature(input_file):
    file_name = os.path.basename(input_file)
    temp_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # print(temp_name)
    temp_name = temp_name + "-create_fake_signatures-" + file_name
    # print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\temp" + "\\" + temp_name

    all_signatures = get_all_file_paths(target_dir=r"D:\毕业设计\example1\signatures")
    """
        for path in all_signatures:
        print(path)
    """
    signature = random.choice(all_signatures)
    # print(signature)
    log1 = "D:\\毕业设计\\example1\\logs\\%s-%s" % (
    "FakeSignatureProcess", time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
    log1 = log1 + ".log"
    command = "python D:\\毕业设计\\example1\\sigthief.py -s %s -t %s -o %s > %s" % (
    signature, input_file, address1, log1)
    # print(command)
    os.system(command)
    os.remove(input_file)
    copy_file(source_address=address1, destination_address=input_file)
    os.remove(address1)
# 添加伪造的签名 但是最后会放置在目标位置
def create_fake_signature_and_output(input_file,output_file):
    all_signatures = get_all_file_paths(target_dir=r"D:\毕业设计\example1\signatures")
    """
        for path in all_signatures:
        print(path)
    """
    signature = random.choice(all_signatures)
    #print(signature)
    log1 = "D:\\毕业设计\\example1\\logs\\%s-%s" % ("FakeSignatureProcess",time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
    log1 = log1+".log"
    command = "python D:\\毕业设计\\example1\\sigthief.py -s %s -t %s -o %s > %s" % (signature,input_file,output_file,log1)
    #print(command)
    os.system(command)

if __name__ == "__main__":
    #create_fake_signature_and_output(r"/sample/sample1.exe", r"D:\毕业设计\example1\sample\sample1_m1.exe")
    init_environment()
    create_fake_signature(r"D:\毕业设计\example1\source_file\sample1.exe")
