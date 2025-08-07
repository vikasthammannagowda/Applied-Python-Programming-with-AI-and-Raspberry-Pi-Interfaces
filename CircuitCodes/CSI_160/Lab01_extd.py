import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

# I am declaring a variable "my_sensor" and initializing it to the physical sensor
my_sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)

I2C_ADDR = 0x27
LCD_COLS = 20 # in my LCD screen i have 20 columns
LCD_ROWS = 4  #
I2C_Port = 1

lcd = CharLCD(i2c_expander = 'PCF8574',
              address = I2C_ADDR,
              port = I2C_Port,
              cols = LCD_COLS,
              rows = LCD_ROWS,
              auto_linebreaks = True)

lcd.clear()# this clears my LCD screen
lcd.cursor_pos = (0,0) # this tells my cursor to display from this point:
#                        (0, 0): (1st row, 1st column )
lcd.write_string(f"Welcome!")

while True:    
    try:
        temperature = my_sensor.temperature # get 
        lcd.cursor_pos = (1,0) # 2nd row and 1st column
        lcd.write_string(f"Temp in C {temperature}")
        
        hum = my_sensor.humidity # 
        lcd.cursor_pos = (3,0) # 4th row, 1st column
        lcd.write_string(f"Humidity is {hum}")
        time.sleep(5)
        lcd.clear()

    except RuntimeError as e:
        print(f"I/O error: {e}")
    except Exception as e:
        my_sensor.exit()
        raise
#time.sleep(2)
