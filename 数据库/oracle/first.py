import cx_Oracle

conn = cx_Oracle.connect('ybgz/ybgz@172.20.3.29:1521/helowin')   #用自己的实际数据库用户名、密码、主机ip地址 替换即可
# conn = cx_Oracle.connect('ybgz', 'ybgz', '172.20.3.29:1521/helowin')
curs = conn.cursor()
sql = 'SELECT * FROM 表名'  # sql语句
rr = curs.execute(sql)
row = curs.fetchone()
print(row[0])
curs.close()
conn.close()
import twisted