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


module_path = os.path.split(os.path.abspath(sys.modules[__name__].__file__))[0]


COMMON_SECTION_NAMES = (
    open(
        os.path.join(
            module_path,
            "section_names.txt",
        ),
    )
    .read()
    .rstrip()
    .split("\n")
)

ALL_SECTION_NAMES = (
    open(
        os.path.join(
            module_path,
            "all_section_names.txt",
        ),
    )
    .read()
    .rstrip()
    .split("\n")
)
COMMON_IMPORTS = json.load(
    open(os.path.join(module_path, "small_dll_imports.json")),
)


class ModifyBinary:
    def __init__(self, bytez):
        self.bytez = bytez

    def _random_length(self):
        return 2 ** random.randint(5, 8)

    def _search_cave(
            self,
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

    def _binary_to_bytez(self, binary, imports=False):
        # Write modified binary to disk
        builder = lief.PE.Builder(binary)
        builder.build_imports(imports)
        builder.build()

        self.bytez = array.array("B", builder.get_build()).tobytes()
        return self.bytez

    def rename_section(self):
        binary = lief.PE.parse(list(self.bytez))
        targeted_section = random.choice(binary.sections)
        # targeted_section.name = random.choice(COMMON_SECTION_NAMES)[:5]
        targeted_section.name = COMMON_SECTION_NAMES[random.randint(0, len(COMMON_SECTION_NAMES)-1)]
        self.bytez = self._binary_to_bytez(binary)
        return self.bytez

    def modify_machine_type(self):

        candidate = [
                lief.PE.MACHINE_TYPES.AMD64,
                lief.PE.MACHINE_TYPES.IA64,
                lief.PE.MACHINE_TYPES.ARM64,
                lief.PE.MACHINE_TYPES.POWERPC,
            ]

        binary = lief.PE.parse(list(self.bytez))

        binary.header.machine = candidate[random.randint(0, len(candidate))]

        self.bytez = self._binary_to_bytez(binary)

        return self.bytez

    def modify_timestamp(self):
        candidate = [
                0,
                868967292,
                993636360,
                587902357,
                872078556,
            ]

        binary = lief.PE.parse(list(self.bytez))

        binary.header.time_date_stamps = candidate[random.randint(0, len(candidate)-1)]

        self.bytez = self._binary_to_bytez(binary)

        return self.bytez
    def append_benign_data_overlay(self):
        begin = random.randint(0,int(len(str1)/2))
        end = random.randint(int(len(str1)/2),len(str1))
        #print
        s1 = str1[begin:end]
        overlay = bytearray(s1,encoding="utf-8")
        #print(overlay)
        self.bytez += overlay
        return self.bytez
    def add_section_benign_data(self):
        begin = random.randint(0, int(len(str1) / 2))
        end = random.randint(int(len(str1) / 2), len(str1))
        s1 = str1[begin:end]
        benign_binary_section_content = bytearray(s1, encoding="utf-8")


        binary = lief.PE.parse(list(self.bytez))

        current_section_names = [section.name for section in binary.sections]
        available_section_names = list(
            set(ALL_SECTION_NAMES) - set(current_section_names),
        )

        if len(available_section_names) == 0:
            available_section_names = random.choice(string.ascii_lowercase)

        section = lief.PE.Section(random.choice(available_section_names))
        section.content = benign_binary_section_content
        binary.add_section(section, lief.PE.SECTION_TYPES.DATA)

        self.bytez = self._binary_to_bytez(binary)
        return self.bytez
    def add_imports(self):
        binary = lief.PE.parse(list(self.bytez))

        # draw a library at random


        # libname = random.choice(list(COMMON_IMPORTS.keys()))
        libnames = list(COMMON_IMPORTS.keys())
        libname = libnames[random.randint(0, len(libnames)-1)]
        funcname = random.choice(list(COMMON_IMPORTS[libname]))
        lowerlibname = libname.lower()

        # find this lib in the imports, if it exists
        lib = None
        for im in binary.imports:
            if im.name.lower() == lowerlibname:
                lib = im
                break

        if lib is None:
            # add a new library
            lib = binary.add_library(libname)

        # get current names
        names = {e.name for e in lib.entries}
        if funcname not in names:
            lib.add_entry(funcname)

        self.bytez = self._binary_to_bytez(binary, imports=True)

        return self.bytez

    def remove_debug(self):
        binary = lief.PE.parse(list(self.bytez))
        if binary.has_debug:
            for i, e in enumerate(binary.data_directories):
                if e.type == lief.PE.DATA_DIRECTORY.DEBUG:
                    e.rva = 0
                    e.size = 0
                    self.bytez = self._binary_to_bytez(binary)
                    return self.bytez
        # no debug found
        return self.bytez

    def modify_optional_header(self):
        binary = lief.PE.parse(list(self.bytez))

        oh = {
            "major_linker_version": [2, 6, 7, 9, 11, 14],
            "minor_linker_version": [0, 16, 20, 22, 25],
            "major_operating_system_version": [4, 5, 6, 10],
            "minor_operating_system_version": [0, 1, 3],
            "major_image_version": [0, 1, 5, 6, 10],
            "minor_image_version": [0, 1, 3],
        }


        keys = list(oh.keys())
        key = keys[random.randint(0,len(keys)-1)]

        modified_val = random.choice(oh[key])
        binary.optional_header.__setattr__(key, modified_val)

        self.bytez = self._binary_to_bytez(binary)
        return self.bytez
    def add_bytes_to_section_cave(self):
        caves = []
        binary = lief.PE.parse(list(self.bytez))
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
                self._search_cave(
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

            self.bytez = (
                    self.bytez[: random_selected_cave[0]]
                    + add_bytes
                    + self.bytez[random_selected_cave[1]:]
            )

        return self.bytez

    def break_optional_header_checksum(self):
        binary = lief.PE.parse(list(self.bytez))
        binary.optional_header.checksum = 0
        self.bytez = self._binary_to_bytez(binary)
        return self.bytez


if __name__ == "__main__":
    # use for testing/debugging actions
    import hashlib

    filename = r"/sample/sample1_m4.exe"
    with open(filename, "rb") as f:
        bytez = f.read()

    m = hashlib.sha256()
    m.update(bytez)
    print(f"original hash: {m.hexdigest()}")


    bi = ModifyBinary(bytez)
    bytez1 =bi.append_benign_data_overlay()
    m = hashlib.sha256()
    m.update(bytez1)
    outputFileName = r"D:\毕业设计\example1\sample\sample1_m4.exe"
    with open(outputFileName,"wb+") as f1:
        f1.write(bytez1)
    print(f"modified hash: {m.hexdigest()}")

    #embed()
