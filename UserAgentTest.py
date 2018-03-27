from urllib import request

if __name__=="__main__":
    url = "http://www.csdn.net/"
    head ={}
    #伪造浏览器的User agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    #创建请求对象
    req = request.Request(url,headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print (html)

