import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

my_sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)

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
lcd.clear()
lcd.cursor_pos = (0,0)
lcd.write_string(f"Welcome!")

    
#print("Hello")
try:
    temperature = my_sensor.temperature
    lcd.cursor_pos = (1,0)
    lcd.write_string(f"Temp in C {temperature}")
    #lcd.cursor_pos = (2,0)
    #temp_f = (temperature * 9/5) + 32
    #lcd.write_string(f"Temp in F {temp_f}")
    #hum = my_sensor.humidity
    #lcd.cursor_pos = (3,0)
    #lcd.write_string(f"Humidity is {hum}")
    #print("Temp:", temperature)
    time.sleep(5)
    lcd.clear()

except RuntimeError as e:
    print(f"I/O error: {e}")
except Exception as e:
    my_sensor.exit()
    raise
#time.sleep(2)
