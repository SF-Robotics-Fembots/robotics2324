import logging 
import subprocess

info = "printenv"
output = subprocess.check_output(info, text=True)

logging.basicConfig(level=logging.INFO, filename = "cameraInfo.log", filemode = "w")
output_line = output.splitlines()

for x in range(0, len(output_line)):
    if "USER=" in output_line[x]:
        result = output_line[x]
        print(result)
        logging.info(output_line[x])

split_result = result.split("=")
name = split_result[1]
print(name)