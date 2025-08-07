from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

speed_factor = 0.15
leds = (led1, led2, led3, led4)

try:

    while True:
        for led in leds:
            led.on()
            sleep(speed_factor)
            led.off()


except KeyboardInterrupt:
    pass
finally:
    for led in leds:
        led.off()
        led.close()

    print("Cleaned up")
