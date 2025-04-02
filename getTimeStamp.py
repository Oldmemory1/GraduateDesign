def getTimeStamp(file):
    import pefile
    import datetime
    pe = pefile.PE(file)
    timestamp = pe.FILE_HEADER.TimeDateStamp
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    print(f"Timestamp: {timestamp} -> {utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")