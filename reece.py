import time
import serial

# Replace 'COMx' with the actual port name on Windows, or '/dev/ttyUSBx' on Linux/Mac.
ser = serial.Serial('/dev/tty.usbserial-DB00NI6A', baudrate=38400)  # Make sure to set the correct baud rate.

def send_command(command):
    ser.write(command)
    time.sleep(1)

def form_letter(finger):
    print("Forming letter") # '{letter}' - Move {finger} to position {position}")
    send_command(finger)
    print("Letter formed!")
    # time.sleep(2)  # Add a 2-second delay after forming each letter

# Send the finger positions for spelling "REECE"
form_letter(b'F2 P0\r\n')    # Move middle finger fully open (letter "R" - Middle finger)
form_letter(b'F1 P0\r\n')    # Move index finger fully open (letter "E" - Index finger)
form_letter(b'F0 P0\r\n')    # Move thumb fully open (letter "E" - Thumb)

form_letter(b'F2 P50\r\n')   # Move middle finger to position 50 (halfway closed - letter "C" - Middle finger)
form_letter(b'F1 P100)\r\n')  # Move index finger fully closed (letter "E" - Index finger)
form_letter(b'F0 P100\r\n')  # Move thumb fully closed (letter "E" - Thumb)

# Close the serial port when done.
ser.close()
