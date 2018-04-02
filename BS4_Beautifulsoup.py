from bs4 import BeautifulSoup
from urllib import request

#创建实例
url = "https://www.jianshu.com/p/78cb574a2750"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
html = resp.read()
resp = html.decode('utf-8')

#创建对象beautifulsoup
bs = BeautifulSoup(resp, 'html.parser')
#bs = BeautifulSoup(html)

#格式化输出print
print (bs.prettify())

#beautifulsoup将复杂的html文档转换为树形结构，每一个节点都是一个对象这些对象可以归纳为

#1. tag, tag相当于html的一个标签
#提取tag
#titles = bs.find_all('title')
#print ("打印", titles)

titles = bs.find_all('h1','title')
for title in titles:
    print ("当前文章标题：", title.string)