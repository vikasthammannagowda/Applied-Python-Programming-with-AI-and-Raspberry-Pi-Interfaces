from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)

try:
    num = int(input("Enter an integer:"))

    # add a while True: to kepp it on
    if(num % 2 == 0):
        print("Even")
        led1.on()
        sleep(3)
    else:
        print("Odd")
        led2.on()
        sleep(3)


except KeyboardInterrupt:
    pass
finally:
    led1.off()
    led1.close()
    led2.off()
    led2.close()
    print("Cleaned up")
