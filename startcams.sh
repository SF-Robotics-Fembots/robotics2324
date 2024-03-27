#!/bin/bash

modprobe uvcvideo quirks=0x80
bash camerarun.sh