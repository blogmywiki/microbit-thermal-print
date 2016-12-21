# sample Python code for thermal printers on BBC micro:bit
# by Giles Booth @blogmywiki / for more information
# see http://www.suppertime.co.uk/blogmywiki/2016/12/microbit-thermal/

import microbit
microbit.uart.init(baudrate=19200, bits=8, parity=None, stop=1, tx=microbit.pin8, rx=None)

# Print lines of text in buffer
def thermal_print_ln(msg):
    microbit.uart.write(msg+"\n")

# Send text but don't print - you need to send a 
# newline (\n) character to empty buffer & print.
# This enables mixed print modes on same line.
def thermal_print(msg):
    microbit.uart.write(msg)

def doubleHeightOn():
    microbit.uart.write("\x1B\x21\x10") 
 
def doubleHeightOff():
    global print_mode
    microbit.uart.write("\x1B\x21\x00") 

def smallFontOn():
    microbit.uart.write("\x1B\x21\x01") 
    
def smallFontOff():
    microbit.uart.write("\x1B\x21\x00") 

def boldOn():
    microbit.uart.write("\x1B\x45\x01") 
    
def boldOff():
    microbit.uart.write("\x1B\x45\x00") 

def wideOn():
    microbit.uart.write("\x1B\x0E") 

def wideOff():
    microbit.uart.write("\x1B\x14") 

def inverseOn():
    microbit.uart.write("\x1B\x21\x02") 
    
def inverseOff():
    microbit.uart.write("\x1B\x21\x00") 

def upsideDownOn():
    microbit.uart.write("\x1B\x7B\x01") 

def upsideDownOff():
    microbit.uart.write("\x1B\x7B\x00") 

def underlineOn():
    microbit.uart.write("\x1B\x2D\x02") 

def underlineOff():
    microbit.uart.write("\x1B\x2D\x00") 

def largeFontOn():
    microbit.uart.write("\x1D\x21\x11") 

def largeFontOff():
    microbit.uart.write("\x1D\x21\x00") 

def leftAlign():
    microbit.uart.write("\x1B\x61\x00")

def centreAlign():
    microbit.uart.write("\x1B\x61\x01")

def rightAlign():
    microbit.uart.write("\x1B\x61\x02")

# prints test page
def printerTest():
    microbit.uart.write("\x12\x54")

# resets the printer to default values
def printerReset():
    microbit.uart.write("\x1B\x40")

def barcodeHumanReadable():
    microbit.uart.write("\x1D\x48\x02")  # print numbers below
    
def barcodeNotHumanReadable():
    microbit.uart.write("\x1D\x48\x00")  # print no numbers

def barcodeUPCA(num):
    microbit.uart.write("\x1D\x6B\x00"+num+"\x00")

def barcodeEAN13(num):
    microbit.uart.write("\x1D\x6B\x02"+num+"\x00")
    
def barcode128(barcode):
    microbit.uart.write("\x1D\x6B\x08"+barcode+"\x00")

def barcode93(barcode):
    microbit.uart.write("\x1D\x6B\x07"+barcode+"\x00")
    
# press button A to activate demo
# increase printing temperature and time
microbit.uart.write("\x1B\x37\x07\xFF\xFF")
while True:
    if microbit.button_a.is_pressed():
        thermal_print_ln("Microbit thermal printer demo")
        centreAlign()
        thermal_print_ln("Centre text")
        rightAlign()        
        thermal_print_ln("right align")
        leftAlign()        
        thermal_print("left align")
        wideOn()
        thermal_print_ln(" Wide text")
        wideOff()
        inverseOn()
        thermal_print("inverse text")
        inverseOff()
        boldOn()
        thermal_print_ln(" bold text")
        boldOff()
        largeFontOn()
        thermal_print_ln("really big font")
        largeFontOff()
        smallFontOn()
        thermal_print_ln("A really very teeny tiny font indeed")
        smallFontOff()
        upsideDownOn()
        thermal_print_ln("upside down text")
        upsideDownOff()
        doubleHeightOn()
        thermal_print_ln("Double height text")
        doubleHeightOff()
        thermal_print_ln("I can print several common barcode formats with or without human-readable numbers")
        thermal_print_ln("UPC-A:")
        barcodeHumanReadable()
        barcodeUPCA("086126100326")
        thermal_print_ln("EAN13:")
        barcodeEAN13("9781477520826")
        barcode128("CODE128")
        barcode93("CODE93")
       
    microbit.sleep(300)
