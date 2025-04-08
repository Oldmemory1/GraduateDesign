import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
if __name__=="__main__":
    list1 = []
    i = 1
    while i<=256:
        list1.append(generate_random_string(2048))
        i = i+1
    print("[")
    for j in list1:
        print("'"+j+"'"+",")
    print("]")
