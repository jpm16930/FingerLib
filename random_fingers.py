

import random
import time
import serial


# Replace 'COMx' with the actual port name on Windows, or '/dev/ttyUSBx' on Linux/Mac.
ser = serial.Serial('/dev/tty.usbserial-DB00NI6A', baudrate=38400)  # Make sure to set the correct baud rate.

def get_random_value(previous_value):
    new_value = previous_value
    while new_value == previous_value:
        new_value = random.randint(0, 4)
    return new_value

def get_random_percentage():
    return random.randint(0, 100)

previous_x = None

try:
    for _ in range(20):  # Replace '5' with the desired number of iterations in the loop.
        x = get_random_value(previous_x)
        yy = get_random_percentage()    

        command = f'F{x} P{yy}\r\n'
        ser.write(command.encode())

        # Add a delay of 0.5 second before sending the next command.
        time.sleep(0.5)

        previous_x = x

except KeyboardInterrupt:
    print("Loop interrupted by the user.")

finally:
    # Close the serial port when done.
    ser.close()
