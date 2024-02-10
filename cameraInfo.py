import os
import subprocess 

print = 'printenv'

os.system(print)
output = subprocess.check_output(["printenv"], text=True)

print(output)