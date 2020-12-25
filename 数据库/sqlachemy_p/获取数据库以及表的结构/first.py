from pyhive import hive
from sqlalchemy.orm import sessionmaker, relationship
from impala.dbapi import connect
from sqlalchemy import create_engine
# from models import Baseinfo
import pymysql
from configparser import ConfigParser
from sqlalchemy.pool import NullPool
import os
path = os.path.dirname(os.path.abspath(__file__))

def mysql_conn():
    cp = ConfigParser()
    cp.read("./config.ini")
    mysql_host = cp.get('mysql2', 'host')
    mysql_port = cp.get('mysql2', 'port')
    mysql_user = cp.get('mysql2', 'user')
    mysql_passwd = cp.get('mysql2', 'passwd')
    mysql_db = cp.get('mysql2', 'db')
    return pymysql.connect(host=mysql_host,
                           port=int(mysql_port),
                           user=mysql_user,
                           passwd=mysql_passwd,
                           db=mysql_db
                           )
engine = create_engine('mysql://', creator=mysql_conn,
                       poolclass=NullPool # 不使用sqlachemy的连接池
                       )
from sqlalchemy.engine import reflection

inspector = reflection.Inspector.from_engine(engine)
for schema in inspector.get_schema_names():
    print(schema)
    # for table in inspector.get_table_names(schema):
    #     print(table)