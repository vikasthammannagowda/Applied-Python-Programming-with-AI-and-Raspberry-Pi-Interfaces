import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        print("LED: ON")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        print("LED: OFF")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("ALL clear")
        
