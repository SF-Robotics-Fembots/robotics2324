import os
import subprocess 
import logging

videos = ["0", "2"]
ports = []
for x in videos:
    command = "/dev/video" + x
    output = subprocess.check_output(["v4l2-ctl", "--all", "-d", command], text=True)

    output_line = output.splitlines()

    for x in range(0, len(output_line)):
        if "Bus info" in output_line[x]:
            result = output_line[x]

    split_result = result.split("-1.")
    name = split_result[1]
    ports.append(name)

info = {
    "port" + ports[0]: "/dev/video"+ videos[0],
    "port" + ports[1]: "/dev/video" + videos[1]
}

subprocess.call(['bash', 'camerarun.sh', info["port" + ports[0]], info["port" + ports[1]]])

