import os
import sys
from subprocess import getoutput
a = getoutput("adb devices")
print ("无设备连接：",a,)

