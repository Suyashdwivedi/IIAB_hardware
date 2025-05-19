#!/usr/bin/env python3
"""
IIAB Shutdown by a switch

Author: Suyash Dwivedi (U:Suyash.dwivedi)
Date: 20/05/2025 
Link: https://en.wikipedia.org/wiki/Internet-in-a-Box

This script safely shuts down a Raspberry Pi-based IIAB system when a
momentary push-button is held down for a specified duration. A status LED
provides visual feedback on startup and button press state.
"""

import time
import subprocess
import RPi.GPIO as GPIO

# ==== Configuration ====
SHUTDOWN_PIN = 23         # GPIO pin number where the push button is connected
STATUS_LED_PIN = 24       # GPIO pin number where the status LED is connected
HOLD_TIME_SECONDS = 5     # Time in seconds the button must be held to trigger shutdown

# ==== Setup GPIO ====

GPIO.setwarnings(False)            # Disable GPIO warnings (in case of reuse)
GPIO.setmode(GPIO.BCM)             # Use Broadcom pin-numbering scheme
GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set button pin as input with internal pull-up resistor
GPIO.setup(STATUS_LED_PIN, GPIO.OUT, initial=GPIO.HIGH)      # Set LED pin as output and turn it ON to indicate system is running

def iiab_shut_down():
    """
    Gracefully shuts down the Raspberry Pi.
    """
    subprocess.run(["sudo", "shutdown", "-h", "now"])  # Executes the system shutdown command

def flash_led(times=5, interval=0.5):
    """
    Flashes the status LED to indicate shutdown is about to occur.
    :param times: Number of flashes
    :param interval: Time in seconds for each ON/OFF flash
    """
    for _ in range(times):
        GPIO.output(STATUS_LED_PIN, False)  # Turn OFF LED
        time.sleep(interval)
        GPIO.output(STATUS_LED_PIN, True)   # Turn ON LED
        time.sleep(interval)

# ==== Main loop ====

try:
    print("IIAB Shutdown Monitor is Running...")  # Optional: print status to terminal
    while True:
        # Check if the button is pressed (logic LOW because of pull-up resistor)
        if GPIO.input(SHUTDOWN_PIN) == GPIO.LOW:
            press_start = time.time()  # Record the time when button is first pressed

            # Wait while the button is still being held down
            while GPIO.input(SHUTDOWN_PIN) == GPIO.LOW:
                time.sleep(0.1)  # Small delay to reduce CPU usage

                # If held long enough, initiate shutdown sequence
                if time.time() - press_start >= HOLD_TIME_SECONDS:
                    flash_led()         # Flash the LED to give feedback to the user
                    iiab_shut_down()    # Shutdown the system
                    break               # Exit inner loop to avoid repeated shutdown

        time.sleep(0.1)  # Polling delay to prevent excessive CPU usage

except KeyboardInterrupt:
    # If script is interrupted (e.g., Ctrl+C), clean up GPIO
    pass

finally:
    # Cleanup all GPIO configurations before exiting
    GPIO.cleanup()
