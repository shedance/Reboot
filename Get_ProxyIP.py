from bs4 import BeautifulSoup
from urllib import request
import random
import os
import re

#def get_ip_list(url, headers):
    #web_data = requests.get(url, headers=headers)
    #soup = BeautifulSoup(web_data.txt, 'lxml')
proxyip = []
url = "http://www.xicidaili.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#请求网页
req = request.Request(url, headers=headers)
page_info = request.urlopen(req)
html = page_info.read()
resp = html.decode('utf-8') #解码后的网页最后用来进行创建beautifulsoup对象
#print (resp)

#创建beautifulsoup对象
#bs = BeautifulSoup(resp,'html.parser')
bs = BeautifulSoup(resp,'html.parser')
table = bs.find('table',attrs={'id':'ip_list'})
tr = table.find_all('tr')[1:]
#print(tr)
#查找需要的标签属性
for item in tr:
    tds = item.find_all('td')
    #print('tds:',list(tds))
    if tds:
        temp_dict = {}
        kinds = '{0}:{1}'.format(tds[1].string, tds[2].string)
        #print(kinds)
        proxyip.append(kinds)
print ("所有的代理IP：",proxyip)

    #ip = tds[1].get_text()
    #port = tds[2].get_text()
    #kind = '{0}:{1}'.format(ip,port)
    #print (kind)
    #temp_dict = {}
    #kind = '{0}:{1}'.format(tds[1].text().lower(), tds[2].text())
    #print(kind)
    #x = proxyip.append(kind)
    #print(x)