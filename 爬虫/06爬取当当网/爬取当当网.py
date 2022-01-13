# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 上午11:03
# @Author  : dataport
# @File    : 爬取当当网.py
# @Software: PyCharm
import requests
import re
import json

# 当当书籍排行网址
# 可以看到每一个每一个书都在一个li标签中
# 通过改变最后一个数字进行翻页
url_dang = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1"


def request_dandan(url):
    """
    获取到爬取网址的内容
    :param url:要爬取的网址
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    """
    对拿到的网址的内容通过正则匹配，进行内容结构化
    :param html: 爬取到的网页内容
    :return:
    """
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_item_to_file(item):
    """
    爬取到的内容写入文件
    :param item: 要写入的数据(每一本书的描述，字典类型)
    :return:
    """
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def main(page):
    """
    对某一页进行爬取
    :param page:要爬取的页码数
    :return:
    """
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)  # 解析过滤我们想要的信息

    for item in items:
        # print(item)
        write_item_to_file(item)


if __name__ == "__main__":
    #  爬取从１页到第25页的地址
    for i in range(1, 26):
        main(i)
