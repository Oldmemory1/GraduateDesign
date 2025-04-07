import pefile
def getCheckSum(input_file):
    pe = pefile.PE(input_file)
    # 获取原始校验和
    original_checksum = pe.OPTIONAL_HEADER.CheckSum
    print(original_checksum)
if __name__== "__main__":
    getCheckSum("HelloWorld2.exe")
    getCheckSum("modifiedHello2.exe")