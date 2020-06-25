# encoding:UTF-8
# @Author: wangzi
import time
import requests
import re
from threading import Thread

#好听轻音乐网---音乐下载


def get_url_pages(url_page):
    for i in range(1):
        print('正在下载第{}页的歌曲'.format(i))

        params = {
        'pageIndex': i,
        'pageSize': '20',
        'order': 'hot'
        }
        url = 'http://www.htqyy.com/genre/4'
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Referer': 'http://www.htqyy.com/genre/4'
        }
        #获取每一页的网页源码
        res_page = requests.get(url_page,headers=headers,params=params)
        return res_page


def get_music(res_page):
    #正则匹配 需要的 id
    id_list = re.findall(r'<span class="title"><a href="/play/(.*?)"',res_page.text,re.S)
    for id in id_list:
        #拼接成所需要的url
        url_ = 'http://f2.htqyy.com/play8/{}/mp3/6'.format(id)
        res_ = requests.get(url_)
        #持久化存储
        with open('music/{}.mp3'.format(id),'wb')as f:
            print('正在下载id为{}的歌曲'.format(id))
            f.write(res_.content)


if __name__ == '__main__':
    start_time = time.time()
    url_page = 'http://www.htqyy.com/genre/musicList/4'
    res_page = get_url_pages(url_page)
    get_music(res_page)
    print('耗时：{}秒'.format(time.time()-start_time))
