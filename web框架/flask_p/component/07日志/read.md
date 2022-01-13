## logging
### 日志级别说明
level的等级	DEBUG < INFO < WARNING < ERROR < CRITICAL

<u>**NOTSET: 不是输出所有日志，而是使用父logger的日志级别**</u>

Debug : 最详细的日志信息,主要的应用场景问题的诊断

Info : 详细程度仅次于debug模式,主要来记录关键节点的信息,确定程序是否正常如预期完成

Warning:当某些不被期望的事情发生的时候,需要记录的信息,比如磁盘即将存满,注意当前的程序一依旧可以正常运行,不报错

Error 出现严重问题,导致某些功能不能正常运行记录信息

Critical: 系统即将崩溃或者已经崩溃
### logging的format配置
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:

%(levelno)s: 打印日志级别的数值

%(levelname)s: 打印日志级别名称

%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]

%(filename)s: 打印当前执行程序名

%(funcName)s: 打印日志的当前函数

%(lineno)d: 打印日志的当前行号

%(asctime)s: 打印日志的时间

%(thread)d: 打印线程ID

%(threadName)s: 打印线程名称

%(process)d: 打印进程ID

%(message)s: 打印日志信息
### flask logging
app.logger

会使用logging.getLogger(app.name)进行logger获取
### 遇到的问题
#### 问题1
logger = logging.getLogger(app.name) 这个定义logger会被父logger(root logger)进行日志过滤

设置logger.propagate = False为取消经过父logger进行日志过滤