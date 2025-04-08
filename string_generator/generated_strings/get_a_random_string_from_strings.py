import random

from string_generator.generated_strings.strings_length_256 import strings_256bytes


def get_random_string(string_list):
    return string_list[random.randint(0,len(string_list)-1)]
if __name__ == "__main__":
    print(get_random_string(string_list=strings_256bytes))