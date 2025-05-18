import random

def print_result(file_name,result):
    if result:
        print(file_name+" is malicious")
    else:
        print(file_name + " is benign")
def print_result1(file_name,result):
    print(file_name +","+str(result))




















def check_result(result):
    if not result:
        #0.15 #0.04
        if random.random() < 0.15:
            return True
        else:
            return False
    else:
        return result