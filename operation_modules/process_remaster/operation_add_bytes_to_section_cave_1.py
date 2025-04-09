import array
import json
import os
import random
import string
import subprocess
import sys
import tempfile
from os import listdir
from os.path import isfile, join
import pefile
import lief
import re
from string1 import str1
from binary_str1 import binaryStr1
def search_cave(
        bytez,
        name,
        body,
        file_offset,
        vaddr,
        cave_size=128,
        _bytes=b"\x00",
):
    found_caves = []
    null_count = 0
    size = len(body)

    for offset in range(size):
        byte = body[offset]
        check = False

        if byte in _bytes:
            null_count += 1
        else:
            check = True

        if offset == size - 1:
            check = True
            offset += 1

        if check:
            if null_count >= cave_size:
                cave_start = file_offset + offset - null_count
                cave_end = file_offset + offset
                cave_size = null_count
                found_caves.append([cave_start, cave_end, cave_size])
            null_count = 0
    return found_caves



def add_bytes_to_section_cave(bytez):
        caves = []
        binary = lief.PE.parse(list(bytez))
        base_addr = binary.optional_header.imagebase
        for section in binary.sections:
            section_offset = section.pointerto_raw_data
            vaddr = section.virtual_address + base_addr
            body = bytearray(section.content)

            if section.sizeof_raw_data > section.virtual_size:
                body.extend(
                    list(b"\x00" * (section.sizeof_raw_data - section.virtual_size)),
                )

            caves.extend(
                search_cave(
                    bytez,
                    section.name,
                    body,
                    section_offset,
                    vaddr,
                ),
            )

        if caves:
            random_selected_cave = random.choice(caves)
            begin = random.randint(0, int(len(str1) / 2))
            end = random.randint(int(len(str1) / 2), len(str1))
            s1 = str1[begin:end]
            benign_binary_section_content = bytearray(s1, encoding="utf-8")
            add_bytes = bytearray(benign_binary_section_content)[:random_selected_cave[-1]]

            # upper = random.randrange(256)
            # add_bytes = bytearray(
            #     random.randint(0, upper) for _ in range(random_selected_cave[-1])
            # )

            bytez1 = (
                    bytez[: random_selected_cave[0]]
                    + add_bytes
                    + bytez[random_selected_cave[1]:]
            )
            return bytez1
        else:
            return bytez
