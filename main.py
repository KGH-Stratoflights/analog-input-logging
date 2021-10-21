from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)


i2c = busio.I2C(board.SCL, board.SDA)
chan = AnalogIn(ads, ADS.P0)
while True:
    print(chan.value, chan.voltage)
    sleep(1)
