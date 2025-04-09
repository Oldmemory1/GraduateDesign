from init.clear_directory import clear_directory

# 清空temp文件夹里的暂存内容
def dump_temp():
    clear_directory(target_dir="./temp")
if __name__=="__main__":
    dump_temp()