from tpa81 import *

thermometer = TPA81()

#compass.changeAdress(0)

print "Version: ", thermometer.softwareVersion()
print "Ambient Temperature: ", thermometer.ambientTemperature()

for i in xrange(len(thermometer.TPA81_PIXEL)):
    print "Pixel", (i + 1), ": ", thermometer.pixelTemp(i)