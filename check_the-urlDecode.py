import chardet
from urllib import request
import urllib
import os
content = input("请输入要查询的网址(例如,www.baidu.com)：")
url = content 
#url = "http://www.ip138.com/"
data = request.urlopen(url).read()
#chardet进行内容分析
chardit1 = chardet.detect(data)
print (chardit1['encoding'])