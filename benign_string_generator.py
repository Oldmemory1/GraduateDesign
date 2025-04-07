import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
if __name__=="__main__":
    print(generate_random_string(8192))
