# IIAB Shutdown by a Switch Python Script

**Author**: Suyash Dwivedi (U:Suyash.dwivedi)  
**Profile**: [Suyash Dwivedi on Meta](https://meta.wikimedia.org/wiki/User:Suyash.dwivedi)

This Python script allows you to safely shut down an **Internet-in-a-Box (IIAB)** device by pressing a momentary push-to-on button connected to a Raspberry Pi's GPIO pin. A status LED indicates the startup of the IIAB device and the button press status.

## Features

- **Safe Shutdown**: When the button is pressed for 5 seconds (configurable), the IIAB device is shut down safely.
- **LED Indicator**: A LED flashes to indicate the status of the shutdown process.
- **Simple Components**: Only three components are required:
  1. Push-to-on button
  2. LED
  3. Resistor (1000 ohms)
  4. Connecting wires
  5. PCB (optional)

## Components Needed

- Raspberry Pi
- Push-to-on button
- LED
- 1000 ohm resistor
- Connecting wires
- Breadboard or PCB (optional)

## Description

This script monitors the button connected to the Raspberry Pi's GPIO pin. When the button is pressed for approximately 5 seconds, the LED will blink, and the IIAB device will safely shut down.

**IIAB**: [Internet-in-a-Box](https://en.wikipedia.org/wiki/Internet-in-a-Box)  
For more information on IIAB and its usage, visit the link provided.

## How to Use

1. **Wiring**: 
   - Connect the push-to-on button to GPIO pin 23 and the LED to GPIO pin 24 on the Raspberry Pi.
   - Ensure the button is configured with an internal pull-up resistor using `GPIO.PUD_UP`.
   
2. **Running the Script**:
   - Run the script on the Raspberry Pi. When you hold down the button for 5 seconds, the LED will blink, and the device will safely shut down.
   
3. **Shutting Down**:
   - The shutdown process will be triggered by holding the button for about 5 seconds. You can modify the time in the script if necessary.

## Installation

1. Clone or download this repository.
2. Install any required libraries, such as `RPi.GPIO`:
   ```bash
   sudo apt-get install python3-rpi.gpio
