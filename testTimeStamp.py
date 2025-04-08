
from operation_modules.operation_modify_timeStamp import modify_pe_timestamp
from datetime import datetime
from getTimeStamp import getTimeStamp

custom_time = datetime(2000, 1, 1).timestamp()
getTimeStamp("input.exe")
modify_pe_timestamp(input_file="input.exe",output_file="output.exe",new_timestamp=int(custom_time))
getTimeStamp("output.exe")