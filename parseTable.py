import subprocess
output = subprocess.check_output("udevadm info -a -p /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3", shell=True)

output = output.decode("utf-8")

print(output)