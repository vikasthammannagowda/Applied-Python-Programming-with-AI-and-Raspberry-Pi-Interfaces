from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)

try:
    chips = int(input("Please enter the number of chips bag:"))
    drink = float(input("Please enter the quantity of drink in floz:"))

    # add a while True: to kepp it on
    if((chips >= 2) and (drink > 32.0)):
        print("Enter!")
        led1.on()
        sleep(5)
    else:
        print("Do not enter!")
        led2.on()
        sleep(5)


except KeyboardInterrupt:
    pass
finally:
    led1.off()
    led1.close()
    led2.off()
    led2.close()
    print("Cleaned up")
