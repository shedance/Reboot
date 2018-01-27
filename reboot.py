import time
import sys
import os

i=0
a = "List of devices attached"
while i < 3:
    i+=1
    devices = os.system("adb devices")
    print devices
    if devices == a:
        break
    time.sleep(20)
    os.system("adb shell date")
    print "Reboot:", i
    os.system("adb reboot")
    time.sleep(30)




