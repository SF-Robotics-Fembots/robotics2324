#!/bin/bash

rmmod uvcvideo
modprobe uvcvideo quirks=0x80
bash focusscript.sh
bash startupcams.sh & python3 main.py && fg
