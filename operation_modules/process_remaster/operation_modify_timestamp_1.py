import random

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez
from timestamp_generator.timestamp_generator import generate_random_timestamp

# 修改时间戳 但是随机生成过去一年之内的任意时间戳
def modify_timestamp(bytez):
    """
    candidate = [
        0,
        868967292,
        993636360,
        587902357,
        872078556,
    ]
    """
    binary = lief.PE.parse(list(bytez))

    binary.header.time_date_stamps = generate_random_timestamp()

    bytez1 = binary_to_bytez(binary)

    return bytez1