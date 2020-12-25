from sqlalchemy.orm import sessionmaker, relationship
from impala.dbapi import connect
from sqlalchemy import create_engine
# from models import Baseinfo
import pymysql
from configparser import ConfigParser
from sqlalchemy.pool import NullPool
import os

path = os.path.dirname(os.path.abspath(__file__))


def impala_conn():
    return connect(host='192.168.50.135',
                   port=10022,
                   database='gkyy_medical_kudu_db',
                   # timeout=20,
                   # use_ssl=True,
                   # ca_cert='some_pem',
                   # user=user, password=pwd,
                   # auth_mechanism='PLAIN'
                   )


def mysql_hie_conn():
    cp = ConfigParser()
    cp.read(path + "/../config.ini")
    mysql_host = cp.get('mysql_hip', 'host')
    mysql_port = cp.get('mysql_hip', 'port')
    mysql_user = cp.get('mysql_hip', 'user')
    mysql_passwd = cp.get('mysql_hip', 'passwd')
    mysql_db = cp.get('mysql_hip', 'db')
    return pymysql.connect(host=mysql_host,
                           port=int(mysql_port),
                           user=mysql_user,
                           passwd=mysql_passwd,
                           db=mysql_db)


def mysql_conn():
    cp = ConfigParser()
    cp.read(path + "/../config.ini")
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


# engine = create_engine('impala://', creator=conn)
engine = create_engine('mysql://', creator=mysql_conn,
                       poolclass=NullPool # 不使用sqlachemy的连接池
                       )
engine_hip = create_engine("mysql://",
                           creator=mysql_hie_conn,
                           # pool_size=20,
                           # max_overflow=30,
                           poolclass=NullPool # 不使用sqlachemy的连接池
                           )

def session():
    Session = sessionmaker(bind=engine)
    session = Session()
    # res = session.query(Baseinfo).limit(10).all()  #查询所有用户,及对应的role id
    return session


def session_hip():
    Session = sessionmaker(bind=engine_hip)
    session = Session()
    return session
