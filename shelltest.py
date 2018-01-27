import os
import commands
var1, var2 = commands.getstatusoutput('adb devices')
print var1, var2
