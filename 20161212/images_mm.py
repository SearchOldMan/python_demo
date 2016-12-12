import urllib
import os

def get_page(url):
    response = urllib.urlopen(url)
    html = response.read().decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    print html[a:b]

def find_img(page_url):
    pass

def save_imgs(folder,img_address):
    pass

def get_images(folder='OOXX',pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'http://jiandan.net/ooxx'
    
    current_page = int(get_page(url))
    
    for i in range(pages):
        current_page -= i
        page_url = url + 'page-' + str(current_page) + '#comments'
        
        img_address = find_img(page_url)
        
        save_imgs = save_imgs(folder,img_address)

if __name__ == '__main__':
    get_images()