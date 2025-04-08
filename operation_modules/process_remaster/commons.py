import json
import os
import sys

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

if __name__ == "__main__":
    for i in COMMON_SECTION_NAMES:
        print(i)
    for j in ALL_SECTION_NAMES:
        print(j)
    for k in COMMON_IMPORTS:
        print(k)