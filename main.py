from virus_scanner_module.clamScanner import clamScanner
# 使用示例
file_to_scan = r"D:\BaiduNetdiskDownload\β6.66_Help小白包V5.5.0：真真的冬\beta6.66TEST31.exe"
is_malicious = clamScanner(file_to_scan)
if is_malicious:
    print("此程序是恶意程序")
else:
    print("此程序是正常程序")
