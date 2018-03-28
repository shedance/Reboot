from urllib import request
import urllib
if __name__=="__main__":
    #my ip is what use the website get
    url2 = "http://www.whatismyip.com.tw/"
    #代理IP
    proxy = {'https':'219.135.164.245:3128'}
    #创建Proxyhandler
    proxy_support = request.ProxyHandler(proxy)
    print ("打印",proxy_support)
    #创建opener
    opener = request.build_opener(proxy_support)
    print ("打印",opener)
    #添加user Agent
    opener.addheaders = [ ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')]
    #安装Opener
    request.install_opener(opener)
    #响应访问的地址url2
    response = request.urlopen(url2)
    #读取相应访问的网址信息并解码
    html = response.read().decode('utf-8')
    print (html)


