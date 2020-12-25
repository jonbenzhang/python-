import requests

proxies = {
    'https': 'http://127.0.0.1:12333',
    'http': 'http://127.0.0.1:12333'
}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}
# http://icanhazip.com 此网址获取当前使用ip
# r = requests.get('http://icanhazip.com', headers=head, proxies=proxies)

r = requests.get('http://www.google.com', proxies=proxies)
print(r.text)
