import requests
from multiprocessing import Pool


def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return url, response.content.decode("utf-8")


def call_back(args):
    url = args[0]
    content = args[1]
    print(url, len(content))


if __name__ == '__main__':
    # 前面必须要加http://
    url_list = ["http://www.baidu.com",
                "http://www.sohu.com",
                "http://www.sogou.com",
                ]
    p = Pool(5)
    for url in url_list:
        p.apply_async(get, args=(url,), callback=call_back)
    p.close()
    p.join()
