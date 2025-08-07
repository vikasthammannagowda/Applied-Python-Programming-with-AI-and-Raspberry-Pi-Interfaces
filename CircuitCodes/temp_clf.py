from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

try:
    temp = float(input("Enter the temperature!"))

    # add a while True: to kepp it on
    if(temp >=95):
        print("Hot")
        led1.on()
        sleep(3)
    elif(temp >=80):
        print("Warm")
        led2.on()
        sleep(3)
    elif (temp >=65):
        print("Good")
        led3.on()
        sleep(3)
    else:
        print("Cool")
        led4.on()
        sleep(3)

except KeyboardInterrupt:
    pass
finally:
    led1.off()
    led1.close()
    led2.off()
    led2.close()
    led3.off()
    led3.close()
    led4.off()
    led4.close()
    print("Cleaned up")
