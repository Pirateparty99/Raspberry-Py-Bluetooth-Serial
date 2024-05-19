#!/usr/bin/env python
import serial
import os
import subprocess
from returns.result import Failure, Success, safe

script_directory="./script"
script_list = []
numbered_script_list = []


def list_script_files(script_directory):
    for script in os.listdir(script_directory):
        print(script)
        script_list.append(script)
    for number, script in enumerate(script_list):
        numbered_script_list.append(number, script)



def user_select_script():
    # Add functionality to print first 9-10 scripts, then add a next page button?
    selected_script = input("Select a script from the list below:" + "\n" + print(numbered_script_list[:9]))
    match selected_script:
        # Print script output, run script
        case 1 | 9:
            subprocess.run(numbered_script_list[selected_script])
        case _:
            print("Not in the list, select a number between 1-9:")
            selected_script
            


# Print to serial prompt to select script, then print output of script to serial:
serial_write = serial.Serial('/dev/ttyS0')  # open serial port
print(serial_write.name)         # check which port was really used
serial_write.write(b'hello')     # write a string
serial_write.close()             # close port


# Read:
with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
     x = ser.read()          # read one byte
     s = ser.read(10)        # read up to ten bytes (timeout)
     line = ser.readline()   # read a '\n' terminated line
ser.close()             # close port
