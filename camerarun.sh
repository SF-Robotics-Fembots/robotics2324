
ustreamer --device=/dev/video0 --host=192.168.1.99 --port=8080 --device-timeout 2 -r 640x480 -b 1
& ustreamer --device=/dev/video1 --host=192.168.1.99 --port=80800 --device-timeout 2 -r 640x480 -b 1 && fg
