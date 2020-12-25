from twisted.web.client import getPage, defer
from twisted.internet import reactor
import requests
import time
def all_done():
    reactor.stop()
# 回调函数
def callback(content):
    print(content)


defer_list = []
url_list = ["https://www.bing.com", "https://www.segmentfault.com/", "https://stackoverflow.com/"]
for url in url_list:
    # time.sleep(2)
    deferred = getPage(bytes(url, encoding="utf-8"))
    deferred.addCallback(callback=callback)
    defer_list.append(deferred)
dlist = defer.DeferredList(defer_list)
dlist.addBoth(all_done)
reactor.run()