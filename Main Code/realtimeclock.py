# sudo pip3 install adafruit-circuitpython-ds3231
# set RTC manually so that we don't reset the time when sat. restarts: sudo hwclock --set --date="Aug-22-2016 18:00:00"
import adafruit_ds3231
import time
import board

i2c = board.I2C()  # uses board.SCL and board.SDA
rtc = adafruit_ds3231.DS3231(i2c)

t = rtc.datetime
print(t)
print(t.tm_hour, t.tm_min)
