import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

# Define the GPIO pin number
pin_number = 21 # Change this to your desired GPIO pin number

# Set up the GPIO pin as an output
GPIO.setup(pin_number, GPIO.OUT)

try:
    while True:
        GPIO.output(pin_number, GPIO.LOW)  # Set pin HIGH
        print("Pin is HIGH")
        time.sleep(1)                        # Wait for 1 second
        
        GPIO.output(pin_number, GPIO.HIGH)   # Set pin LOW
        print("Pin is LOW")
        time.sleep(1)                        # Wait for 1 second

except KeyboardInterrupt:
    pass  # Exit the loop on Ctrl+C

finally:
    GPIO.cleanup()  # Clean up GPIO settings
