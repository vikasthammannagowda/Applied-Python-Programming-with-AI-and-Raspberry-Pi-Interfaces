from gpiozero import LED
from time import sleep
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

# ODD or EVEN checker

try:
    # declare a variable and get user input and convert to integer
    user_input = int(input("Please enter a integer:"))

    # clear the lcd
    lcd.clear()

    # set LCD cursor position to 1st row (0th index)
    #                      and 1st column (0th index)
    lcd.cursor_pos = (0,0)
    # display the input value on the LCD
    lcd.write_string(f"The input is {user_input}")
    lcd.cursor_pos = (2, 0)
    if((user_input % 2) == 0): # condition for an integer to be even
        
        # set LCD cursor position to 3rd row and 1st column
        #lcd.cursor_pos = (2, 0)
        # display the result
        lcd.write_string(f"{user_input} is EVEN!")

    else:
        # set LCD cursor position to 3rd row and 1st column
        # Note: we are setting the cursor to the same position 
        #       since only one of these two (if or else) will execute
        #lcd.cursor_pos = (2, 0)
        # display the result
        lcd.write_string(f"{user_input} is ODD!")
        



except KeyboardInterrupt:
    pass
finally:
    print("Done!")
