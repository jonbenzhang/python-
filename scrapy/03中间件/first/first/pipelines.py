# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
源码内容：
    1. 判断当前XdbPipeline类中是否有from_crawler
        有：
            obj = XdbPipeline.from_crawler(....)
        否：
            obj = XdbPipeline()
    2. obj.open_spider()

    3. obj.process_item()/obj.process_item()/obj.process_item()/obj.process_item()/obj.process_item()

    4. obj.close_spider()
"""
from scrapy.exceptions import DropItem


class FilePipeline(object):

    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        print('File.from_crawler')
        path = crawler.settings.get('HREF_FILE_PATH')
        return cls(path)

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        # if spider.name == 'chouti':
        print('File.open_spider')
        self.f = open(self.path, 'a+')

    def process_item(self, item, spider):
        # f = open('xx.log','a+')
        # f.write(item['href']+'\n')
        # f.close()
        print('File', item['content'])
        self.f.write(item['content'] + '\n')
        # 返回item,下面的定义的DbPipeline才会执行
        # return item
        # raise DropItem(),下面定义的DbPipeline不会执行
        raise DropItem()

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('File.close_spider')
        self.f.close()


class DbPipeline(object):
    def __init__(self, path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        print('DB.from_crawler')
        path = crawler.settings.get('HREF_DB_PATH')
        return cls(path)

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('Db.open_spider')
        self.f = open(self.path, 'a+')

    def process_item(self, item, spider):
        # f = open('xx.log','a+')
        # f.write(item['href']+'\n')
        # f.close()
        print('Db', item)
        # self.f.write(item['href']+'\n')
        return item

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('Db.close_spider')
        self.f.close()
