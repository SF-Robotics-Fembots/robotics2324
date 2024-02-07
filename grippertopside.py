import hid, json, socket
import time
from mcp2210 import Mcp2210, Mcp2210GpioDesignation, Mcp2210GpioDirection

#reading each hid device in the json as a string, it stores EACH string in an enum w/ each device having
#own index

#hid = human interface deviceS

vendor_id = 0x04D8
product_id = 0x00DE
#enum creates a list where the first item in the list is either a 0
device_list = hid.enumerate(vendor_id, product_id)
#device_list_dumped = json.dumps(device_list)
print(device_list)
print(type(device_list))
#sn = list(device_list[0].values())[3]
print(type(device_list[0]))
#print(type(sn))

#serial_number = device_list_dumped
serial_number = device_list[0]["serial_number"]
print(serial_number)

# connect to the device by serial number
mcp = Mcp2210(serial_number)

# this only needs to happen once
# if you don't call this, the device will use the existing settings
mcp.configure_spi_timing(chip_select_to_data_delay=0,
                         last_data_byte_to_cs=0,
                         delay_between_bytes=0)

#port for the socket
port = 40000

def main(ip_server):
    print(ip_server)

    #set up a server socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip_server, port))
    serversocket.listen(1)
    print("socket listening")

   

    # set all pins as GPIO
    for i in range(9):
        mcp.set_gpio_designation(i, Mcp2210GpioDesignation.GPIO)

    # set 2 to input
    mcp.set_gpio_direction(1, Mcp2210GpioDirection.INPUT)

    (clientconnected, clientaddress) = serversocket.accept()
    #the while 1 acts as a while true
    x = mcp.get_gpio_value(1)
    while True:
        prevx = x
        x = mcp.get_gpio_value(1)
        print(x)
        if x == False:
            message = "a"
            print(message)
        if x == True:
            message = "b"
            print(message)
        if prevx != x:
            data  = message.encode()
            clientconnected.send(data)
        time.sleep(0.1)



        # flash an LED
        # set_gpio_output_value(<pin_number>,<on or off>)
        #mcp.set_gpio_output_value(0, False)
        #for i in range(3):
           # mcp.set_gpio_output_value(0, True)
           # time.sleep(0.5)
           # mcp.set_gpio_output_value(0, False)
           # time.sleep(0.5)

        # LED slider
        #counter = 0
        #for _ in range(20):
         #   counter += 1
          #  counter %= 5
           # for i in range(5):
            #    mcp.set_gpio_output_value(i, counter == i)
            #time.sleep(0.2)

        # turn all LEDs off
        #for i in range(0, 5):
         #   mcp.set_gpio_output_value(i, False)

        # set pin 4 as CS, and transmit the bytes 0 through to 255 inclusive over SPI
        #mcp.set_gpio_designation(4, Mcp2210GpioDesignation.CHIP_SELECT)
        #tx_data = bytes(range(256))
        #rx_data = mcp.spi_exchange(tx_data, cs_pin_number=4)

        # as MOSI is connected to MISO, check that the data matches what we sent
        #assert rx_data == tx_data

    

    
        



#call the main method
if __name__ == "__main__":
    main()