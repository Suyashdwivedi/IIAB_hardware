# iiab_shutdown.py
#
# =============================================================================
#                 IIAB Shutdown by a switch Python Script
# =============================================================================
# WRITTEN BY: Suyash Dwivedi (U:Suyash.dwivedi)
# DATE: 14/08/2021
# The hackathon of Wikimania 2021
# https://wikimania.wikimedia.org/wiki/2021:Hackathon/Participants
# 
#    Refrence
#    Kevin Godden
#    https://www.ridgesolutions.ie/index.php/2013/02/22/raspberry-pi-restart-shutdown-your-pi-from-python-code/
#
# ==================== DESCRIPTION AND HOW TO USE ====================
# This python script allow to safely shutdown A device through a momentary push-to-on button conntcte to GPIO pin
# A LED helps to indicate proper startup of IIAB device and also indicate status of button press 
# Link to IIAB: https://en.wikipedia.org/wiki/Internet-in-a-Box
# How to use: Holding down the button for about 5 seconds (You can change) LED fill flash and IIAB will be shutdown safely.
# It needs only three components and connecting wires 
# (1)Push to on button (2) LED (3) Resistance (1000 ohms) (4)connecting wires (5) PCB (optional)
# Distributed as-is; no warranty is given
# -----------------------------------------------------------------------------

import time
import RPi.GPIO as GPIO

# Pin definition
iiab_shutdown_pin = 23
status_led_pin = 24

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# using a momentary push button without a pull up resistor (using internal pullup).

GPIO.setup(iiab_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(status_led_pin, GPIO.OUT)
GPIO.output(status_led_pin, True)

# function to shutdown IIAB
def iiab_shut_down():
  # uncomment this line to see status on command line
  # print ('IIAB shutting down')
    time.sleep(1)
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
  # uncomment this line to see status on command line
  # print (output)

while True:
  # uncomment this line to see status on command line
  # print ('IIAB is Running')
    if GPIO.input(iiab_shutdown_pin) == False:
        counter = 0
  #  on holding down the button LED will flash 5 times then after 1 second IIAB device will be shutdown.
        while GPIO.input(iiab_shutdown_pin) == False:     
            counter += 5
            GPIO.output(status_led_pin, False)
            time.sleep(1)
            GPIO.output(status_led_pin, True)
            time.sleep(1)
            GPIO.output(status_led_pin, False)

            # long button press
            if counter > 6:
                iiab_shut_down()
# =============================================================================
#                 IIAB Shutdown by a switch Python Script end
# =============================================================================