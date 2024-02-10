import os
import subprocess 

print = 'printenv'

os.system(print)
output = subprocess.check_output(["os.system(print)"], text=True)
print("\n" + output)