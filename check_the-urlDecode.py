import chardet
from urllib import request
import urllib
import os
content = input("请输入要查询的网址(例如,www.baidu.com)：")
url = content
#url = "http://www.ip138.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
req = request.Request(url, headers=headers)
data = request.urlopen(req).read()
#chardet进行内容分析
chardit1 = chardet.detect(data)
print (chardit1['encoding'])

