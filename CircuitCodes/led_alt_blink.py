import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

LED_PIN_1 = 27
GPIO.setup(LED_PIN_1, GPIO.OUT)

my_time = .1

try:
    while True:
        print("LED1: ON")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(my_time)
        print("LED1: OFF")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(my_time)
        print("LED2: ON")
        GPIO.output(LED_PIN_1, GPIO.HIGH)
        time.sleep(my_time)
        print("LED2: OFF")
        GPIO.output(LED_PIN_1, GPIO.LOW)
        time.sleep(my_time)


except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("ALL clear")
        
