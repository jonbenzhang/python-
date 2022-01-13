import logging
from logging.handlers import RotatingFileHandler
from flask_old import Flask

app = Flask(__name__)


def log_init(app):
    # 如果不加app.name，就会获取到root_logger
    # root_logger的日志级别也会对app.logger进行过滤
    logger = logging.getLogger(app.name)

    """
    log日志的level如下
    _nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,}
    # """
    logger.setLevel(logging.DEBUG)
    # 是否通过把logger的日志传递到父logger进行日志过滤,
    # True为传递到父logger日志,False为不传递到父logger日志
    # 如果不设置为False就会通过root logger进行过滤,root logger的默认level为WARNING
    logger.propagate = False
    # print(logging.root.setLevel(10))
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('test.log', encoding='utf-8')

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    # 设置输出到控制台的日志级别
    ch.setLevel(logging.DEBUG)
    # 设置format格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 设置写入文件的日志级别
    fh.setLevel(logging.INFO)
    # 设置写入文件format方式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # print(fh.level)
    # print(ch.level)
    # print(logger.level)
    # 添加输出对象
    # logger对象可以添加多个fh和ch对象
    logger.addHandler(fh)
    logger.addHandler(ch)

log_init(app)
# app.logger.notset('NOTSET')
app.logger.debug('DEBUG')
app.logger.info('INFO')
app.logger.warning('WARNING')
app.logger.error('ERROR')
app.logger.critical('CRITICAL')
# print(app.logger.name)
