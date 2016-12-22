#coding=utf-8
'''
煎蛋网的爬虫图片下载
http://jandan.net/ooxx/page-2281#comments
图片来源：
<img src="//ww3.sinaimg.cn/mw600/005vbOHfgw1faypuux4bgj30fz0rfq96.jpg" style="max-width: 480px; max-height: 750px;">

page：
<span class="current-comment-page">[2281]</span>
'''
import urllib
import os

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
def url_open(url):
    response = urllib.urlopen(url, head)
    html = response.read()
    return html

#获取第几页函数
def get_page(url):
    html = url_open(url)

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]
#图片地址列表
def find_imgs(page_url):
    html = url_open(page_url)
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(a+9,b+4)
        else:
            b = a+9
        a = html.find('img src',b)
    return img_addrs
#图片保存到文件夹函数
def save_imgs(filename,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

#下载函数
def download_img(filename='ooxx',pages=10):
    #建立文件夹
    os.mkdir('E:\\learngit\\python_demo\\20161222\\'+filename)
    os.chdir(filename)
    url = 'http://jandan.net/ooxx/'
    #下载图片
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(filename,img_addrs)

if __name__ == '__main__':
    download_img()