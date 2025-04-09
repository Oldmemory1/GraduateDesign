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

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez
from operation_modules.process_remaster.commons import COMMON_IMPORTS
from string1 import str1
from binary_str1 import binaryStr1


def add_imports(bytez):
    binary = lief.PE.parse(list(bytez))

    # draw a library at random

    # libname = random.choice(list(COMMON_IMPORTS.keys()))
    libnames = list(COMMON_IMPORTS.keys())
    libname = libnames[random.randint(0, len(libnames) - 1)]
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
    bytez1 = binary_to_bytez(binary, imports=True)
    return bytez1
