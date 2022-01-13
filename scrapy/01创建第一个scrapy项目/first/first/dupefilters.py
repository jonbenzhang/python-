"""
修改去重规则
如要使用此去重规则，需要在配置文件中进行配置
# 修改默认的去重规则
# DUPEFILTER_CLASS = 'first.dupefilters.zhangDupeFilter'
"""

from scrapy.dupefilters import BaseDupeFilter

from scrapy.utils.request import request_fingerprint


class zhangDupeFilter(BaseDupeFilter):

    def __init__(self):
        self.visited_fd = set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        # request_fingerprint 通过请求request对象生成的一个字符串
        # www.baidu.com/?a=1&b=2和www.baidu.com/?b=2＆a=1两个url生成的字符串相同
        # www.baidu.com/?a=1&b=2和www.baidu.com/?b=2＆a=1两个url生成的字符串相同
        fd = request_fingerprint(request=request)
        if fd in self.visited_fd:
            return True
        self.visited_fd.add(fd)

    def open(self):  # can return deferred
        print('开始')

    def close(self, reason):  # can return a deferred
        print('结束')

    # 　每爬取一个url都会执行一次
    def log(self, request, spider):  # log that a request has been filtered
        print('日志')
