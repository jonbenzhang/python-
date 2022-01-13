##爬虫代理
### 爬虫代理方法1(request)
使用环境变量,在环境变量添加自己的代理服务器地址
```
export http_proxy="http://127.0.0.1:12333"
export https_proxy="http://127.0.0.1:12333"```
```

### 爬虫代理方法2(request)
```
proxies = {
    'https': 'http://127.0.0.1:12333',
    'http': 'http://127.0.0.1:12333'
}
# http://icanhazip.com 此网址获取当前使用ip
# r = requests.get('http://icanhazip.com', proxies=proxies)
r = requests.get('http://www.google.com', proxies=proxies)
```
