import serial
import time

# Replace 'COMx' with the actual port name on Windows, or '/dev/ttyUSBx' on Linux/Mac.
ser = serial.Serial('/dev/tty.usbserial-DB00NI6A', baudrate=38400)  # Make sure to set the correct baud rate.

# Send the command 'G0' to the hand.
ser.write(b'G1 C\r\n')

# Add a delay of 1 second before sending the next command.
time.sleep(1)

# Send the next command (example: 'G1' in this case).
ser.write(b'F1 P50\r\n')

# Add a delay of 1 second before sending the next command.
time.sleep(1)

# Send the next command (example: 'G1' in this case).
ser.write(b'G1 O\r\n')

# Close the serial port when done.
ser.close()

