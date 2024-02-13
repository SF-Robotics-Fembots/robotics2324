import os
import subprocess 
import logging

info = "printenv"
output = subprocess.check_output(info, text=True)

logging.basicConfig(level=logging.INFO, filename = "cameraInfo.log", filemode = "w")

output_line = output.splitlines() #splits data into lines?

for x in range(0, len(output_line)): #goes through each linr and check is there is mention of "user"
    if "user" in output_line[x]:
        print(output_line[x])
        logging.info(output_line[x])

    elif "USER" in output_line[x]:
        print(output_line[x])
        logging.info(output_line[x])

   # separate = output_line[x].split() #should split the line into each word
   # for i in range(0, len(separate)):
        

