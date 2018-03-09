from urllib import request
from urllib import parse
import json

if __name__ == "__main__" :
    Request_URL = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    From_Data = {}
    From_Data['i'] = "你好"
    From_Data['from'] = "AUTO"
    From_Data['to'] = "AUTO"
    From_Data['smartresult'] = "dict"
    From_Data['client'] = "fanyideskweb"
    From_Data['salt'] = "1520393684312"
    From_Data['sign'] = "33fae6fa33188f53f16df6721ed754ea"
    From_Data['doctype'] = "json"
    From_Data['version'] = "2.1"
    From_Data['keyfrom'] = "fanyi.web"
    From_Data['action'] = "FY_BY_REALTIME"
    From_Data['typoResult'] = "false"

    data = parse.urlencode(From_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    print (translate_results)
3    translate_results = translate_results['translateResult'][0][0]['tgt']
    print ("FYJG：%s" % translate_results)