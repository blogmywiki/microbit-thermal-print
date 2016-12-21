# microbit-thermal-print
MicroPython code to print from a BBC micro:bit to a thermal till-roll printer

![alt text](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/12/thermal-demo.jpg)

## Introduction
A long time ago I made several printing gizmos with a Sparkfun thermal till-roll printer, driven by an Arduino or a 
Raspberry Pi. 
I thought it might be fun to see if I could drive the printer using a humble BBC micro:bit and some Python, and by golly 
you can.

## How to build one

To get this working you will need:
* a BBC micro:bit powered off batteries or a computer.
* a Chinese thermal till-roll printer as sold by Pimoroni, Sparkfun, Adafruit etc.
* a 5-9v 2A DC power supply for the printer.
* some jumper leads and a breakout board like the Kitronik one.
* an old soap powder box or similar to mount the printer and micro:bit in.

Please note that I have only tested this code with a printer I bought many years ago, firmware version 2.64 - some of the 
features may not work on your printer, you should check with its manual to see if you need to alter any of the codes.

The wiring diagram looks a bit like this:

![alt text](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2016/12/microbit-thermal-print_bb2.png)

## To-do list
* add options for barcode height and width
* add line-spacing and print-density options
* bitmap graphics and user-defined characters
* get binary masking working to enable better mixing of modes
* make a Python module out of the code
