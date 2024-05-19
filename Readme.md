# Raspberry Py Bluetooth Serial
This project uses the Python pySerial library to create a serial connection on a Raspberry Pi for transmitting over the Adafruit BLE Friend UART device. The BLE Friend is used to wirelessly transmit a UART connection via BLE to be received by another BLE-capable device. The goal of this project is to be able to connect a BLE Friend to a Raspberry Pi Zero 2W so that the Raspberry Pi can be remotely controlled. This project is intended to be used initially with a Flipper Zero as the device used to control the Raspberry Pi, but this (hopefully) will be usable with any other device connecting to the BLE UART Friend/Raspberry Pi.

** NOTE: This project is still a work in progress and under development. The code is not fully functional at this time. **

Link to store page for the BLE UART Friend board by Adafruit: 
[BLE UART Friend Store Page](https://www.adafruit.com/product/2479)

Link to the documentation for the pySerial library:
[pySerial Documentation](https://pySerial.readthedocs.io/en/latest/)