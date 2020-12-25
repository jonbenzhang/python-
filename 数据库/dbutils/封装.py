import pymysql
from dbutils.pooled_db import PooledDB


def mysql_conn():
    host = "10.20.1.24"
    port = "3307"
    database = "test2"
    username = "sguser"
    passwd = "python1python"
    return pymysql.connect(host=host,
                           port=int(port),
                           user=username,
                           passwd=passwd,
                           db=database
                           )


class MyDbutils():
    def __init__(self):
        self.pool = PooledDB(
            # 使用impyla为
            # from impala import dbapi
            # creator= dbapi,
            # 使用链接数据库的模块
            creator=pymysql,
            # 连接池允许的最大连接数，0和None表示不限制连接数
            maxconnections=None,
            # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            mincached=2,
            # 链接池中最多闲置的链接，0和None不限制
            maxcached=5,
            # 链接池中最多共享的链接数量，0和None表示全部共享。
            # 因为pymysql和MySQLdb等模块的 threadsafety都为1，
            # 所有值无论设置为多少，maxcached永远为0，所以永远是所有链接都共享。
            maxshared=3,
            # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            blocking=True,
            # 一个链接最多被重复使用的次数，None表示无限制
            maxusage=None,
            # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            setsession=[],
            # ping MySQL服务端，检查是否服务可用。
            #  如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            ping=0,
            # 主机地址
            host='10.20.1.24',
            # 端口
            port=3307,
            # 数据库用户名
            user='sguser',
            # 数据库密码
            password='python1python',
            # 数据库名
            database='count',
            # 字符编码
            charset='utf8'
        )

    def query(self, sql, *args):
        result = []
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            # 执行结果
            cursor.execute(sql, args)
            result = cursor.fetchall()
            # 将conn释放,放回连接池
            conn.close()
        except Exception as e:
            print("查询失败！")
            return e
        return result

    def alter(self, sql, *args):
        count = 0
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            # 执行结果
            count = cursor.execute(sql, args)
            conn.commit()
            conn.close()
        except Exception as e:
            print("提交事物失败！")
            conn.close()
            conn.rollback()
        return count


if __name__ == '__main__':
    dbutils = MyDbutils()
    b = dbutils.alter("insert into t1 (name) values (%s)", 1)
    print(b)
