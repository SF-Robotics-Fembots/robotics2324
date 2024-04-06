#!/bin/bash

rmmod uvcvideo
modprobe uvcvideo quirks=0x80
bash focusscript.sh
nice -n -19 bash startupcams.sh & python3 main.py && fg
