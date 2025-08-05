from gpiozero import LED
from time import sleep

# Create an LED object for each GPIO pin
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

speed_factor = 0.15  # delay (in seconds) between LEDs

try:
    # Infinite loop to light LEDs in sequence
    while True:
        for led in (led1, led2, led3, led4):
            led.on()
            sleep(speed_factor)
            led.off()
except KeyboardInterrupt:
    # Allows you to stop the program with Ctrl+C
    pass
finally:
    # Cleanup: ensure all LEDs are off and resources freed
    for led in (led1, led2, led3, led4):
        led.off()
        led.close()
    print("Cleaned up")
