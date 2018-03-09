import time
import sys
import os
import subprocess

i=0
a = "error: no devices/emulators found"
os.system("adb kill-server")
os.system("adb devices")
while i < 3:
    i+=1
    devices = subprocess.call("adb devices")
    print ("##",devices)
    if devices == 1:
        print ("无VR设备连接到PC，或者设备没有开启USB调试功能")
        break
    time.sleep(20)
    print (os.system("adb shell date"))
    print ("Reboot:", i)
    os.system("adb reboot")
    time.sleep(30)




