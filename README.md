Python-TPA81
=============

A small class to interface with the TPA81 Thermopile Array Module on the Raspberry Pi.

## Examples
This repository includes a couple of examples showing how to read and configure the themopile array.

## Pins
You can use [this](https://www.element14.com/community/servlet/JiveServlet/previewBody/73950-102-11-339300/pi3_gpio.png) image for reference.

| Name | Pin # | Pin name   |
|------|-------|------------|
| SDA  | 03    | GPIO02     |
| SCL  | 05    | GPIO03     |
| GND  | Any   | Any Ground |
| 5V   | Any   | Any 5V     |

## Usage
Import the class by importing TPA81 in the top of your script. For more info see the examples.