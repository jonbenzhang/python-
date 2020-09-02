# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午11:27
# @Author  : dataport
# @File    : 04协程爬虫.py
# @Software: PyCharm
from gevent import monkey

monkey.patch_all()
import requests
import gevent


def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return len(response.content.decode("utf-8"))
    else:
        return 0


if __name__ == '__main__':
    # 前面必须要加http://
    url_list = ["http://www.baidu.com",
                "http://www.sohu.com",
                "http://www.sogou.com",
                ]
    gevent_list = []
    for url in url_list:
        g = gevent.spawn(get_url, url)
        gevent_list.append(g)
    gevent.joinall(gevent_list)
    for i in gevent_list:
        print(i.value)
