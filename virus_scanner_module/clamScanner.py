import pyclamd
def clamScanner(file_path):
    try:
        # 连接到ClamAV的TCP服务（默认端口3310）
        cd = pyclamd.ClamdNetworkSocket(host='127.0.0.1', port=3310)

        # 检查连接是否存活
        if not cd.ping():
            raise ConnectionError("Service is not alive")

        # 执行文件扫描
        scan_result = cd.scan_file(file_path)

        if scan_result is None:
            #print("[safe]")
            return False
        else:
            virus_name = scan_result[file_path][1]
            #print(f"[malicious type]:{virus_name}")
            return True

    except pyclamd.ConnectionError:
        print("Exception: ClamAV service is not running or port is wrong")
    except FileNotFoundError:
        print("Exception: File is not found")
    except Exception as e:
        print(f"Unknown error：{str(e)}")
    return False
if __name__ == "__main__":
    file1 = r"D:\BaiduNetdiskDownload\β6.66_Help小白包V5.5.0：真真的冬\beta6.66TEST31.exe"
    b1 = clamScanner(file1)
    print(b1)
    file2 = r"D:\graduate_design\example1\source_file\sample1.exe"
    b2 = clamScanner(file2)
    print(b2)