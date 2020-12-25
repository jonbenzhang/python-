#!/usr/bin/python
# -*- coding:utf-8 -*-
from impala.dbapi import connect
import sys


def impala_conn_exec(sql):
    conn = connect(host='192.168.x.xx', port=21050)
    cur = conn.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()
    return data_list


sql = "select pk_value,send from  intf_trade_log t where pk_value='00033015017DC9F468FF0E9ABD8A582C'"
now_num = impala_conn_exec(sql)
print(now_num)
