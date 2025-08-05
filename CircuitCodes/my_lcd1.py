import time
from RPLCD.i2c import CharLCD

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

try:
    lcd.clear()
    lcd.write_string("I am not yet done! \n Push past your limits!")
    #time.sleep(5)
finally:
    print("hi")
    #lcd.clear()
