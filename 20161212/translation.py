#coding=utf-8
import urllib
import urlparse
import json
content = raw_input(unicode('请输入内容:','utf-8'))

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.urlencode(data).encode('utf-8')

response = urllib.urlopen(url,data)
html = response.read().decode('utf-8')
target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])