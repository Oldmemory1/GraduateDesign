import os
import random
import string




def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
if __name__=="__main__":
    list1 = []
    i = 1
    while i<=8:
        list1.append(generate_random_string(1048576))
        i = i+1
    output_str = ""
    output_str = output_str + "["
    for j in list1:
        output_str = output_str +"'"
        output_str = output_str + j
        output_str = output_str + "'"
        output_str = output_str + ","
    output_str =output_str + "]"
    file_path = "1048576.txt"
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(output_str)
    file.close()
