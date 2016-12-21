# transmits accelerometer, compass and temperature data every 10 seconds
# by Giles Booth @blogmywiki

from microbit import *
import radio

compass.calibrate()
# remove next line to save power
display.scroll('transmitting data', wait=False, loop=True)
radio.on()

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    tx_message = str(temperature())+"c  head "+str(compass.heading())+"\nx"+str(x)+" y"+str(y)+" z"+str(z)
    radio.send(tx_message)
    sleep(10000)
