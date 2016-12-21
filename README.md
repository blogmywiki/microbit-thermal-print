# microbit-thermal-print
MicroPython code to print from a BBC micro:bit to a thermal till-roll printer

![alt text](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/12/thermal-demo.jpg)

## Introduction
A long time ago I made several printing gizmos (like [The Little Box of Poems](http://www.suppertime.co.uk/blogmywiki/little-box-of-poems/)) with a Sparkfun thermal till-roll printer, driven by an Arduino or a 
Raspberry Pi. 
I thought it might be fun to see if you can drive the printer using a humble BBC micro:bit and some Python, and by golly 
you can!

## How to build one

To get this working you will need:
* a BBC micro:bit powered off batteries or a computer.
* a Chinese thermal till-roll printer as sold by Pimoroni, Sparkfun, Adafruit etc.
* a 5-9v 2A DC power supply for the printer.
* some jumper leads and a micro:bit breakout board like the Kitronik one.
* an old soap powder box or similar to mount the printer and micro:bit in.

Please note that I have only tested this code with a printer I bought many years ago, firmware version 2.64 - some of the 
features may not work on your printer, you should check with its manual to see if you need to alter any of the codes.

The wiring diagram looks a bit like this:

![alt text](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/12/microbit-thermal-print_bb2.png)

Flash the Python code thermal_print.py on to your micro:bit using the [Mu editor](https://codewith.mu).

## How to use the code

I've written functions to cover most text modes. Note that *mixing* text modes doesn't always work because I've had problems getting binary masking to work - that's something I hop to fix later. Each function just sends hex codes to the printer to enable or disable each mode.

The most important functions are `thermal_print("text")` and `thermal_print_ln("text")`

`thermal_print("text")` sends some text to the printer buffer but doesn't print it. It won't print anything until it receives a newline character `\n`. This function allows you to mix some different text modes on the same line.

The more useful function is `thermal_print_ln("text")` which will print a line with anything inside the brackets - it must be a string, and you do not need to add the newline character, the function does this for you.

Other functions are fairly obvious, you have the following modes available:
* left, right, centre align `leftAlign()` `centreAlign()` `rightAlign()`
* bold text `boldOn()` `boldOff()` 
* underline (hard-coded to a thick line) `underlineOn()` `underlineOff()`
* inverse (white on black) text `inverseOn()` `inverseOff()`
* double-width `wideOn()` `wideOff()`
* double-height `doubleHeightOn()` `doubleHeightOff()`
* extra large font `largeFontOn()` `largeFontOff()`
* extra small font `smallFontOn()` `smallFontOff()`
* upside-down text `upsideDownOn()` `upsideDownOff()`
* barcodes in various formats

## Printing barcodes

Four common barcode formats are supported: UPC-A (American Univeral Product code, must be 12 digits), EAN-13 (common European product barcode), Code 128 and Code 93. The last two formats support alphanumeric characters, not just numbers. It's not possible at the moment to specify the height or width of the barcode (I'm working on this), but you can add or supress human-readable numbers below the barcode with the `barcodeHumanReadable()` and `barcodeNotHumanReadable()` functions.

## Wireless printing

You can also set up a thermal printer to work wirelessly with the micro:bit. The `wireless_print_server.py` file polls for incoming radio messages and prints anything it receives. Messages need to be short I've found. You can put the `wireless_data_logger.py` file on another micro:bit which will then transmit data about its x, y and z accelerometer readings plus temperature and compass heading every 10 seconds. When you first run it you have to calibrate the compass by tilting the micro:bit to draw a circle.

## More information 

See my [blog post] (http://www.suppertime.co.uk/blogmywiki/2016/12/microbit-thermal/) for more background information and links to my other internet-connected thermal printing projects. I'd love to hear if you have ideas about how this can be used. I've made a box that prints random poems and Christmas cracker jokes - what can you think of?

## To-do list
* add options for barcode height and width
* add line-spacing and print-density options
* bitmap graphics and user-defined characters
* get binary masking working to enable better mixing of modes
* make a Python module out of the code
* hello to Jason Isaacs
