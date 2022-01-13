from urllib.parse import urlparse  # python2 is from urlparse import urlparse
from urllib.parse import urlsplit  # python2 is from urlparse import urlsplit
from urllib.parse import urljoin  # python2 is from urlparse import urljoin
from urllib.parse import parse_qs  # python2 is from urlparse import parse_qs

# 1.urlparse
# urlparse is used to Parse(解析) url
url_change = urlparse('https://i.cnblogs.com/EditPosts.aspx?opt=1')
# parse result
# scheme(协议)，netloc(域名)，path(路径)，params(可选参数)，query(查询,get请求参数)，fragment(特殊锚)
# ParseResult(scheme='https', netloc='i.cnblogs.com', path='/EditPosts.aspx', params='', query='opt=1', fragment='')
print(url_change)
print(parse_qs(url_change.query))
# 对查询参数,转为字典类型
# {'opt': ['1']}
# 2.urlsplit
# 和urlparse差不多，将url分为5部分，只是少了一个params(可选参数)
url_change2 = urlsplit('https://i.cnblogs.com/EditPosts.aspx?opt=1')
# parse result
# scheme(协议)，netloc(域名)，path(路径)，query(查询,get请求参数)，fragment(特殊锚)
# SplitResult(scheme='https', netloc='i.cnblogs.com', path='/EditPosts.aspx', query='opt=1', fragment='')
print(url_change2)


# 3.urljoin
# url 拼接
# if Second parameter(参数) start with "/",while be remove
new_url = urljoin('https://baidu.com/ssss/', '88888')
print(new_url)


# 4.parse_qs
# 对查询参数(,get请求参数),转为字典类型,注意返回的value值为list类型
print(parse_qs("a=b&c=3"))
# {'a': ['b'], 'c': ['3']}

print(urlparse("http://t.weather.itboy.net/api/weather/city/101030100").hostname)
print(urlparse("http://[fe80::822a:a8ff:fe49:470c%tESt]:1234/keys").hostname)