import os
import subprocess 
import logging

info = "printenv"
#info = "gci env:"
output = subprocess.check_output(info, text=True)

logging.basicConfig(level=logging.INFO, filename = "cameraInfo.log", filemode = "w")

output_line = output.splitlines() #splits data into lines?

for x in range(0, len(output_line)): #goes through each linr and check is there is mention of "user"
    if "USER=" in output_line[x]:
        result = output_line[x]
        print(result)
        logging.info(output_line[x])

split_result = result.split("=")
name = split_result[1]
print(name)
   # separate = output_line[x].split() #should split the line into each word
   # for i in range(0, len(separate)):
        

