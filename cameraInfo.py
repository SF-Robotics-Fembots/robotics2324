import os
import subprocess 

#info = "printenv" - use for unbuntu
info = "dir Env:"
output = str(subprocess.check_output(info, text=True))

print("\n\n\n")
print(output)
