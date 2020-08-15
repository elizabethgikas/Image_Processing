#Program to write the date and IP address to the lcd display
#lcd_display_string(string text, line) will write text to the display
#lcd_clear() will clear the text on the display

import lcddriver
import time
import datetime
import subprocess

display = lcddriver.lcd()
display.lcd_clear()
ip_address = subprocess.check_output(["hostname", "-I"]).split()[0]

try:
    while True:
        display.lcd_display_string("Date: " + str(datetime.datetime.today()), 1)
        display.lcd_display_string("IP: " + str(ip_address), 2)
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

        
        
    