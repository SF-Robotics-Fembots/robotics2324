#!/bin/bash

rmmod uvcvideo
modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80
bash focusscript.sh
bash camerarun.sh 0 & sleep 5 
bash camerarun.sh 2 & sleep 5 
bash camerarun.sh 4 & sleep 5 
bash camerarun.sh 6
