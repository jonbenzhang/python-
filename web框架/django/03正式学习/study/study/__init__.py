import pymysql

# django3.1.1默认使用mysqlclient ,
# mysqlclient运行速度更快，是c写的编译可能有问题
# 因为哦pymysql没有那个版本所以强行修改
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
