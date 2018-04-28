import re
import urllib.request
from bs4 import BeautifulSoup

url='http://findicons.com/pack/2787/beautiful_flat_icons'
page = urllib.request.urlopen(url)
data = page.read()
data = data.decode('utf-8')

#提取页面的图片连接
k = re.split(r'\s+',data)
#print ("=======",k)
s = []
sp = []
si = []
for i in  k:
    if (re.match(r'src',i) or re.match(r'href',i)):
        if(not re.match(r'href="#"',i)):
            if (re.match(r'.*?png"',i) or re.match(r'.*?ico"',i)):
                if (re.match(r'src',i)):
                    s.append(i)
#print('+++++++++++++++++=',s)
for it in  s:
    if (re.match(r'.*?png"',it)):
        sp.append(it)
#print ("================\n",sp)
cnt =0
cou =1
for item in sp:
    m = re.search(r'src="(.*?)"',item) #使用re.search函数将匹配分组后续使用group得到需要的字符
    #print (m)
    #print(type(m.group()))
    itemurl = m.group(1) #之前分组为1，即括号内的内容
    #print(itemurl)
    if(itemurl[0]=='/'):
        continue;
    web = urllib.request.urlopen(itemurl)
    itdata = web.read()
    if (cnt>=6 and cou<=30):
        f = open('F:\\MerciGo\\Reports\\image\\'+str(cou)+'.png',"wb")
        cou = cou+1
        f.write(itdata)
        f.close()
    cnt = cnt +1
