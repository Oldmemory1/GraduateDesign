import os
import random
import time

from findAllSignatures import get_all_file_paths


def create_fake_signature(input_file,output_file):
    all_signatures = get_all_file_paths(r"D:\毕业设计\example1\signatures")
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
    create_fake_signature(r"D:\毕业设计\example1\before\HelloWorld1.exe",r"D:\毕业设计\example1\destination_file\HelloWorld1.exe")
