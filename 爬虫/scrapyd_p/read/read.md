# scrapyd
scrapy项目部署运行的工具
### 安装
```shell script
pip install scrapyd
```
### 配置文件
1.  配置文件模板见同级目录
2. scrapyd 寻找配置文件的位置,如果没有则会使用包中的默认的配置文件，按顺序寻找
* /etc/scrapyd/scrapyd.conf (Unix)
* c:scrapydscrapyd.conf (Windows)
* etc/scrapyd/conf.d/* (in alphabetical order, Unix)
* scrapyd.conf
* ~/.scrapyd.conf (users home directory)

### 启动命令
直接输入scrapyd就可以运行,scrapyd服务，配置文件会按照上面的描述进行查找
```shell script
scrapyd
```
### 通过api接口来控制
#### 1. 查看scrapyd的当前状态daemonstatus.json
curl http://0.0.0.0:6800/daemonstatus.json

返回数据:
{"node_name": "zhangmengcomputer", "status": "ok", "pending": 0, "running": 0, "finished": 0}
* node_name:主机名称
* status:运行状态
* pending:表示等待被调度的任务
* runing:表示正在运行的scrapy任务
* finished:表示已经完成的scrapy任务
   
#### 2.项目部署addversion.json

curl http://0.0.0.0:6800/addversion.json  -F project=myproject -F version=r23 -F egg=@myproject.egg

POST请求：
* project（string，required） 项目名
* version（string，required）项目名版本
* egg（file，required）项目的egg文件（-F egg=@文件地址）
返回:
    {"status":"ok","spiders":3}
    status　ok表示成功
    spiders 3表示成功部署的爬虫数量
#### 3. 启动已经部署好的scrapy代码
curl http://0.0.0.0:6800/schedule.json  -d project=first spider=baidu
* project 为项目名称
* spider 为爬虫名称
 返回
 {"status":"ok","jobid":"132asd1f3a2sd1f32ads1fasd1a"}
 * jobid为当前正在运行爬取任务的代号，id
#### 4. 取消爬虫任务
curl http://0.0.0.0:6800/schedule.json  -d project=first spider=baidu　-d　job=132asd1f3a2sd1f32ads1fasd1a
* project 为项目名称
* spider 为爬虫名称
* job 为爬取任务的代号id
 返回
 {"status":"ok","prevstate":"running"}
 * prevstate :为停止前的运行状态
#### 5. 检查服务的负载状态(daemonstatus.json接口)

curl http://localhost:6800/daemonstatus.json
#### 6. 获取上传到此Scrapy服务器的项目列表(listprojects.json接口)

curl http://localhost:6800/listprojects.json
#### 7. 删除服务器上的项目（delproject.json接口）

curl http://localhost:6800/delproject.json -d project=project_name
## scrapyd-client
### 安装
```shell script
pip install python-client
```
方便把scray项目部署到,scrapyd
### 命令
这是直接部署scrapy代码到scrapyd项目的命令

直接在scrapy项目运行scrapyd-deploy，就可以根据scrapy.cfg文件，配置的scrapyd的地址部署
```shell script
scrapyd-deploy
scrapyd-deploy --version 20201125 (version: 为版本号,不能带字母(可以不设置,默认为当前时间案的时间戳))
```
每个scrapy代码都有scrapy.cfg文件
```shell script
[deploy:vm1]
#可配置要部署的srapyd地址的别名,如上面设置了别名为vm1
#则需要使用代码scrapyd-deploy　vm1来部署到服务器上
# 如果不设置则直接运行scrapyd-deploy即可
url = http://localhost:6800/
project = first
```
* url: 要部署代码的scrapyd地址，
* project: 为项目名称，
## scrapyd API
通过使用scrapyd_api，库来使用代码控制scrapyd
### 安装
```shell script
pip install python-scrapyd-api
```
### 使用
scrapyd所有的api接口的命令都可以通过python代码实现,更多查看官方文档
```python
from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI ('http: //localhost:6800')
#获取当前已经部署的素有项目
print(scrapyd.list_projects())
# 远程部署
#读取要部署的项目的egg文件
egg= open('weibo.egg', 'rb')
scrapyd .add_version('weibo','v1', egg)
```
## scrapyt 
类似scrapyd不支持分布式


## gerapy
