import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
app = Flask(__name__)
# 日至等级的设置
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler('logs.txt', maxBytes=1024 * 1024, backupCount=10)
# 设置日志的格式           日志等级     日志信息文件名   行数        日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)
app.logger.info('你好啊')