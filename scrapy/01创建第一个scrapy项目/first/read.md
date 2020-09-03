# scrapy
安装scrapy包使用anaconda 不要使用pip(pip有报错)
学习使用scrapy版本2.3.0
## 1.创建一个scrapy项目
1. 创建一个名为first的scrapy项目
```
scrapy startproject first
```
2. 创建后的项目结构
``` 
       
└── first    #项目名称
    ├── first   #项目同名文件夹
    │   ├── __init__.py
    │   ├── items.py　　# 持久化
    │   ├── middlewares.py # 中间件
    │   ├── pipelines.py  　#持久化
    │   ├── settings.py   # 配置文件，写爬虫时使用
    │   └── spiders       # 写爬虫文件所在的文件夹
    │       ├── baidu.py　# 如下面创建爬虫的命令，就会生成一个baidu.py
    │       ├── __init__.py

    └── scrapy.cfg　# 主配置文件，项目部署时使用

```

## 2.在此项目创建一个爬虫
1. baidu 为创建的爬虫名
2. www.baidu.com为要爬取的网址
3.创建对应的py文件，路径为first/first/spiders/baidu.py
```
scrapy genspider baidu www.baidu.com
```
## 3 爬虫启动
1. baidu 为要启动的爬虫的名称
```shell script
scrapy crawl baidu
```
2. 不显示爬虫日志
```shell script
scrapy crawl baidu --nolog
```
## 4.爬虫配置
```
1. robots 协议　是否遵守爬虫协议
2. 如果为True,print无显示，
ROBOTSTXT_OBEY = False
```
