#!/bin/bash

rmmod uvcvideo
modprobe uvcvideo quirks=0x80
bash focusscript.sh
bash camerarun.sh & bash camerarun2.sh & bash camerarun3.sh & python3 main.py && fg
