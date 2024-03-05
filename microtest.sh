#!/bin/bash
#test microstreamer script

echo testing microstreamer!

ustreamer --device=/dev/video0 --host=192.168.1.99 --port=8080 --device-timeout 2 -r 800x600 -b 1

#-d , device
#-h , host ip
#-p , port #
#-r , resolution
#-b , buffer (min 1)
