#coding=utf-8
'''
访问的有道翻译网站是http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.top

网页访问User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
'''
import urllib
import json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.top'
data = {}
head = {}
proxies = {'http': '61.166.40.216:8998'}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
content = input('请输入你要翻译的内容:')
'''
data is  dict
type:AUTO
i:i love fishc
doctype:json
xmlVersion:1.8
keyfrom:fanyi.web
ue:UTF-8
action:FY_BY_CLICKBUTTON
typoResult:true
'''
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.urlencode(data).encode('utf-8')

response = urllib.urlopen(url,data,head)
html = response.read()
'''
{"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"i love you","tgt":"我爱你"}]],"smartResult":{"type":1,"entries":["","我爱你。"]}}   -----json
'''
translateContent = json.loads(html)
html = translateContent['translateResult'][0][0]['tgt']

print html

