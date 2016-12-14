#coding=utf-8

import urllib
import json
from BeautifulSoup import BeautifulSoup as bs3

def get_content_from_jd(keyword,page=1):
    params = {'keyword':keyword,'page':page,'area':1,'enc':'utf-8'}
    data = urllib.urlencode(params)
    f = urllib.urlopen('https://search.jd.com/Search?'+data)
    
    content = f.read()
    
    
    f.close()
    
    return content





'''
价格接口
https://p.3.cn/prices/mgets?callback=jQuery9240088&type=1&area=16_1303_48716_48765&skuIds=J_1341478187%2CJ_11029667934%2CJ_10879267443%2CJ_1152395333%2CJ_10782403709%2CJ_1330873480%2CJ_10516121487%2CJ_1633613356%2CJ_10434497597%2CJ_1713190066%2CJ_10500408156%2CJ_1271267648%2CJ_10473577134%2CJ_1760486779%2CJ_1362792338%2CJ_10350919544%2CJ_10749484519%2CJ_11000933684%2CJ_10160570925%2CJ_10733164724%2CJ_10359162198%2CJ_10550197783%2CJ_1017987717%2CJ_1794510650%2CJ_10534266651%2CJ_10127741404%2CJ_10399419006%2CJ_10691021534%2CJ_10196443938%2CJ_10987841701%2CJ_10509770176%2CJ_10674743224%2CJ_10884041492%2CJ_1657572293%2CJ_10629356426%2CJ_10473577134%2CJ_10603942848%2CJ_10618662584%2CJ_1029361162%2CJ_10583386167%2CJ_10637633380%2CJ_1603413058%2CJ_10765980499%2CJ_1749541216%2CJ_10573444337%2CJ_1208828723%2CJ_10550197783&pdbp=0&pdtk=&pdpin=jd_409491ca0a2b8&pduid=853206645&_=1481686225489
'''
def get_price_from_id(*ids):
    
    params = {'skuIds':','.join(['_J%s'%id for id in ids]),'type':1}
    
    data = urllib.urlencode(params)
    opener = urllib.urlopen('https://p.3.cn/prices/mgets?'+data)
    response = opener.read()
    #把字符串转化成json可以识别的格式
    prices = json.loads(response)
    opener.close()
    return prices

if __name__ == '__main__':
    
    content = get_content_from_jd('裤子',page=2)
    try:
        soup = bs3(content)
     
    except Exception as e:
        print e
    else:
        
        mids = soup.find_all(class_='dorpdown')
        print mids
        ids = [mid['sku'] for mid in mids]
        prices = get_price_from_id(ids)
    
        print prices
    
    