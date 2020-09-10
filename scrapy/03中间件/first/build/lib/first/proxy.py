# by luffycity.com
"""
代理使用自定义
需要在setting中进行配置
"""
import base64
import random
from six.moves.urllib.parse import unquote
try:
    from urllib2 import _parse_proxy
except ImportError:
    from urllib.request import _parse_proxy
from six.moves.urllib.parse import urlunparse
from scrapy.utils.python import to_bytes

class FirstProxyMiddleware(object):

    def _basic_auth_header(self, username, password):
        user_pass = to_bytes(
            '%s:%s' % (unquote(username), unquote(password)),
            encoding='latin-1')
        return base64.b64encode(user_pass).strip()

    def process_request(self, request, spider):
        PROXIES = [
            "http://root:woshiniba@192.168.11.11:9999/",
            "http://root:woshiniba@192.168.11.12:9999/",
            "http://root:woshiniba@192.168.11.13:9999/",
            "http://root:woshiniba@192.168.11.14:9999/",
            "http://root:woshiniba@192.168.11.15:9999/",
            "http://root:woshiniba@192.168.11.16:9999/",
        ]
        url = random.choice(PROXIES)

        orig_type = ""
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

        if user:
            creds = self._basic_auth_header(user, password)
        else:
            creds = None
        request.meta['proxy'] = proxy_url
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic ' + creds


class DdbProxyMiddleware(object):
    def process_request(self, request, spider):
        PROXIES = [
            {'ip_port': '111.11.228.75:80', 'user_pass': ''},
            {'ip_port': '120.198.243.22:80', 'user_pass': ''},
            {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
            {'ip_port': '101.71.27.120:80', 'user_pass': ''},
            {'ip_port': '122.96.59.104:80', 'user_pass': ''},
            {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
        ]
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])
            encoded_user_pass = base64.b64encode(to_bytes(proxy['user_pass']))
            request.headers['Proxy-Authorization'] = to_bytes('Basic ' + encoded_user_pass)
        else:
            request.meta['proxy'] = to_bytes("http://%s" % proxy['ip_port'])