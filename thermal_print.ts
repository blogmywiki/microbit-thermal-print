// sample JavaScript code for thermal printers on BBC micro:bit
// original Python code by Giles Booth @blogmywiki
// converted to JavaScript by Niels Swinkels
// for more information see
// http://www.suppertime.co.uk/blogmywiki/2016/12/microbit-thermal/

input.onButtonPressed(Button.A, () => {
    print("Microbit thermal printer demo")
    centreAlign()
    print("Centre text")
    rightAlign()
    print("right align")
    leftAlign()
    print("left align")
    wideOn()
    print(" Wide text")
    wideOff()
    inverseOn()
    print("inverse text")
    inverseOff()
    boldOn()
    print(" bold text")
    boldOff()
    largeFontOn()
    print("really big font")
    largeFontOff()
    smallFontOn()
    print("A really very teeny tiny font indeed")
    smallFontOff()
    upsideDownOn()
    print("upside down text")
    upsideDownOff()
    doubleHeightOn()
    print("Double height text")
    doubleHeightOff()
    print("I can print several common barcode formats with or without human-readable numbers")
    print("UPC-A:")
    barcodeHumanReadable()
    barcodeUPCA("086126100326")
    print("EAN13:")
    barcodeEAN13("9781477520826")
    barcode128("CODE128")
    barcode93("CODE93")
})
function print(msg: string) {
    serial.writeLine(msg)
}
function doubleHeightOn() {
    serial.writeString("\x1B\x21\x10")
}
function doubleHeightOff() {
    serial.writeString("\x1B\x21\x00")
}
function smallFontOn() {
    serial.writeString("\x1B\x21\x01")
}
function smallFontOff() {
    serial.writeString("\x1B\x21\x00")
}
function boldOn() {
    serial.writeString("\x1B\x45\x01")
}
function boldOff() {
    serial.writeString("\x1B\x45\x00")
}
function wideOn() {
    serial.writeString("\x1B\x0E")
}
function wideOff() {
    serial.writeString("\x1B\x14")
}
function inverseOn() {
    serial.writeString("\x1B\x21\x02")
}
function inverseOff() {
    serial.writeString("\x1B\x21\x00")
}
function upsideDownOn() {
    serial.writeString("\x1B\x7B\x01")
}
function upsideDownOff() {
    serial.writeString("\x1B\x7B\x00")
}
function underlineOn() {
    serial.writeString("\x1B\x2D\x02")
}
function underlineOff() {
    serial.writeString("\x1B\x2D\x00")
}
function largeFontOn() {
    serial.writeString("\x1D\x21\x11")
}
function largeFontOff() {
    serial.writeString("\x1D\x21\x00")
}
function leftAlign() {
    serial.writeString("\x1B\x61\x00")
}
function centreAlign() {
    serial.writeString("\x1B\x61\x01")
}
function rightAlign() {
    serial.writeString("\x1B\x61\x02")
}
// prints test page
function printerTest() {
    serial.writeString("\x12\x54")
}
// resets the printer to default values
function printerReset() {
    serial.writeString("\x1B\x40")
}
function barcodeHumanReadable() {
    // print numbers below
    serial.writeString("\x1D\x48\x02")
}
function barcodeNotHumanReadable() {
    // print no numbers
    serial.writeString("\x1D\x48\x00")
}
function barcodeUPCA(num: string) {
    // must be 12 digits long
    serial.writeString("\x1D\x6B\x00" + num + "\x00")
}
function barcodeEAN13(num: string) {
    serial.writeString("\x1D\x6B\x02" + num + "\x00")
}
function barcode128(barcode: string) {
    serial.writeString("\x1D\x6B\x08" + barcode + "\x00")
}
function barcode93(barcode: string) {
    serial.writeString("\x1D\x6B\x07" + barcode + "\x00")
}
serial.redirect(
    SerialPin.P0,
    SerialPin.P1,
    BaudRate.BaudRate19200
)
// increase printing temperature and time
print("\x1B\x37\x07\xFF\xFF")
