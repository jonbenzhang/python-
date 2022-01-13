
import pymysql
from MySQLdb import escape
s:bytes = escape("1 or 1 = 1")
print(s,type(s))
print(s.decode("utf-8"))
print(pymysql.escape_string("1 or 1 = 1"))
