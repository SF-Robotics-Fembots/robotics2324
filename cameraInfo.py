import os
import subprocess 

info = os.system("printenv")
output = subprocess.check_output(info, text=True)

print("\n\n\n")
print(output)