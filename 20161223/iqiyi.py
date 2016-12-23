#coding=utf-8
'''

<li data-indexfocus-index="1" class="">
    <a rseat="fcs_0_t1" href="http://www.iqiyi.com/a_19rrh9s4yl.html" class="thumbnail_item " alt="无间道：黑白之战一触即发" target="_blank">无间道：黑白之战一触即发</a>
</li>
<meta name="description" lang="zh-CN" content="爱奇艺（iQIYI.COM）是全球领先的提供海量、优质、高清的网络视频服务的大型视频网站，网络视频播放首选平台。爱奇艺影视内容丰富多元，涵盖电影、电视剧、动漫、综艺、生活、音乐、搞笑、财经、军事、体育、片花、资讯、微电影、儿童、母婴、教育、科技、时尚、原创、公益、游戏、旅游、拍客、汽车、纪录片、爱奇艺自制剧等剧目。视频播放清晰流畅，操作界面简单友好，真正为用户带来“悦享品质”的在线观看体验。">
'''
import urllib,re

response = urllib.urlopen('http://www.iqiyi.com','r')

#target = re.compile('<a rseat="(fcs_0_t1)" class="thumbnail_item" alt="(.*?)" target="_blank">.*</a>')
target = re.compile('<meta name="(.*?)" lang="zh-CN" content="(.*?)">')
html = response.read()

for name,content in target.findall(html):
    print '%s (%s)' % (name,content)
