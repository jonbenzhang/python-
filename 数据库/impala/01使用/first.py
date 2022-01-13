#!/usr/bin/python
# -*- coding:utf-8 -*-
from impala.dbapi import connect
import sys


def impala_conn_exec(sql):
    conn = connect(host='172.20.3.22', port=21050,database="gkyy_medical_kudu_db")
    cur = conn.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()
    return data_list


sql = "select * from baseinfo"
now_num = impala_conn_exec(sql)
print(now_num)
