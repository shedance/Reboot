import urllib.request
import chardet

#if __name__=="__main__":
    #response = request.urlopen("http://cd.58.com/")
    #html = response.read()
    #chardet = chardet.detect(html)
    #print (chardet)
    #html = html.decode("utf-8")
    #print (html)
url = 'http://cd.58.com/'
response = urllib.request.Request(url=url)
html = urllib.request.urlopen(response)
print (html.getcode())
print (html.headers)