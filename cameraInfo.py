import os
import subprocess 

info = 'printenv'

os.system(info)
output = subprocess.check_output("printenv", text=True)

print(output)