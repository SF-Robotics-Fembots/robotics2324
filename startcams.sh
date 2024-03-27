#!/bin/bash
rmmod uvcvideo
modprobe uvcvideo quirks=0x80
bash camerarun.sh