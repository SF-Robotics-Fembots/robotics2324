#!/bin/bash

rmmod uvcvideo
modprobe uvcvideo quirks=0x80
bash focusscript.sh
bash camerarun.sh 0 & sleep 1 
bash camerarun.sh 2 & sleep 1 
bash camerarun.sh 4 & sleep 1 
bash camerarun.sh 6
