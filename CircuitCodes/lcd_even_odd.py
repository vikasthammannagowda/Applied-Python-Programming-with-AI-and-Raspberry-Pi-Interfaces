from gpiozero import LED
from time import sleep

import time
from RPLCD.i2c import CharLCD

def scroll_text(text, row = 0, delay = 0.3):
    padding = " " * 20
    window = padding + text + padding
    for i in range(len(text) + 20):
        lcd.cursor_pos = (row, 0)
        lcd.write_string(window[i : i + 20])
        time.sleep(delay)

I2C_ADDR = 0x27
LCD_COLS = 20
LCD_ROWS = 4
I2C_Port = 1

lcd = CharLCD(i2c_expander = 'PCF8574',
              address = I2C_ADDR,
              port = I2C_Port,
              cols = LCD_COLS,
              rows = LCD_ROWS,
              auto_linebreaks = True)

led1 = LED(17)
led2 = LED(27)

try:
    num = int(input("Enter an integer:"))
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string(f"The input number is: {num}")
    #scroll_text(f"The input number is: {num}", row = 0)
    # add a while True: to kepp it on
    if(num % 2 == 0):
        #print("Even")
        
        lcd.cursor_pos = (2,0)
        lcd.write_string(f"{num} is even!")
        led1.on()
        sleep(5)
    else:
        #print("Odd")
        
        lcd.cursor_pos = (2,0)
        lcd.write_string(f"{num} is odd!")
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
