import pefile
def get_all_sections_name(file):
    pe = pefile.PE(file)
    section_names = []
    for section in pe.sections:
        section_names.append(section.Name.decode().split('\x00')[0])
    return section_names
if __name__ == "__main__":
    list1 =get_all_sections_name("HelloWorld2.exe")
    for i in list1:
        print(i)