# this will print any radio messages received
# by Giles Booth @blogmywiki

from microbit import *
import radio

uart.init(baudrate=19200, bits=8, parity=None, stop=1, tx=pin8, rx=None)

radio.on()
while True:
    incoming = radio.receive()
    if incoming:
        uart.write(incoming+"\n\n\n")
