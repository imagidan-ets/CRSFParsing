import sys
sys.path.append("/home/imagidan/.local/lib/python3.8/site-packages")

import time
import serial

print("UART Demonstration Program")

serial_port = serial.Serial(
    port="/dev/ttyTHS0",
    baudrate=420000,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

time.sleep(1)

try:

    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.read()
            print(data)
            serial_port.write(data)

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass