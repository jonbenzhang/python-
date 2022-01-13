import requests
import bs4

# 修改请求体内容
payload = {'key1': 'value1', 'key2': 'value2'}
# 修改请求头
headers = {
    'Origin': 'http://quotes.toscrape.com/page/1/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
}
# 设置请求的cookies
r = requests.get('http://quotes.toscrape.com/page/1/', headers=headers)
print(r.status_code)
print(r.text)

