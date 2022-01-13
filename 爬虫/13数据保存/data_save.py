import pymysql
pymysql.connections
from dbutils.pooled_db import PooledDB
import os

DB_HOST = os.environ.get("MYSQL_HOST", '10.20.1.24')
DB_PORT = int(os.environ.get("MYSQL_PORT", '3307'))
DB_USER = os.environ.get("MYSQL_USER", 'sguser')
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", 'python1python')
DB_DATABASE_NAME = os.environ.get("MYSQL_DATABASE_NAME", 'spider')
# DB_TABLE_NAME = os.environ.get("MYSQL_TABLE_NAME", 'COVID_19')
DB_TABLE_NAME = os.environ.get("MYSQL_TABLE_NAME", 't188')


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
            host=DB_HOST,
            # 端口
            port=DB_PORT,
            # 数据库用户名
            user=DB_USER,
            # 数据库密码
            password=DB_PASSWORD,
            # 数据库名
            database=DB_DATABASE_NAME,
            # 字符编码
            charset='utf8'
        )

    def query(self, sql, *args):
        print(sql, args)
        result = []
        conn = self.pool.connection()
        try:
            # 设置查询返回为key,value
            # impyla 为dictify=True
            # pymysql为pymysql.cursors.DictCursor
            cursor = conn.cursor()
            # 执行结果
            # 执行结果
            if args:
                cursor.execute(sql, args[0])
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            # 将conn释放,放回连接池
            conn.close()
        except Exception as e:
            print("查询失败！")
            print(e)
            return e
        return result

    def alter(self, sql, *args):
        print(sql,args)
        count = 0
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            # 执行结果
            if args:
                count = cursor.execute(sql, args[0])
            else:
                count = cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as e:
            print("提交事物失败！")
            conn.close()
            conn.rollback()
        return count


mybatis = MyDbutils()


def table_create(data):
    if (DB_TABLE_NAME,) in mybatis.query("show tables"):
        return
    sql = "create table {_table_name}( default_primary_key_id int(12) not null auto_increment, ".format(
        _table_name=DB_TABLE_NAME)
    for i in data:
        sql += i + " varchar(255), "
    sql += "primary key(default_primary_key_id)) "
    # 创建table
    print(sql)
    mybatis.alter(sql)


def update_data(data: dict, dedup_fields: list):
    sql1 = f'SELECT count(*)from {DB_TABLE_NAME} where {" and ".join(["%s=%%s" % key for key in dedup_fields])}'
    count = mybatis.query(sql1, [data[i] for i in dedup_fields])[0][0]
    if count > 0:
        sql2 = f'UPDATE {DB_TABLE_NAME} SET {" , ".join(["%s=%%s" % key for key in data.keys()])} WHERE {" and ".join(["%s=%%s" % key for key in dedup_fields])};'
        mybatis.alter(sql2, list(data.values())+[data[i] for i in dedup_fields])
        return True
    return False


def save_data(data: dict, dedup_fields=[]):
    table_name = DB_TABLE_NAME
    # 1. 判断是否需要创建数据库表结构
    table_create(data)
    # 2. 判断数据库中是否有完全一样的数据,有的话就不进行处理了
    sql1 = f'SELECT count(*)from {table_name} where {" and ".join(["%s=%%s" % key for key in data.keys()])}'
    count = mybatis.query(sql1, [str(i) for i in data.values()])[0][0]
    if count > 0:
        return
    # 3.去重字段判断,如有去重字段重复的字段则进行数据更新,否则继续
    if dedup_fields:
        if update_data(data, dedup_fields):
            return
    sql2 = f'INSERT INTO {table_name}({",".join(data.keys())}) VALUES ({",".join(["%s" for _ in data.values()])});'
    mybatis.alter(sql2, [str(i) for i in data.values()])


if __name__ == '__main__':
    save_data("t4", {"a": 1, "b": 3})
    # print(mybatis.query("show tables"))
    # table_name = "p"
    # columns =['1','2','3']
    # sql_str = f'INSERT INTO {table_name}({",".join(columns)}) VALUES ({",".join(["%s" for _ in columns])});'
    # print(sql_str)
