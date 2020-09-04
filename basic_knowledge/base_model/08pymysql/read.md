## 增删改
1.　增删改必须要进行commit,否则修改不会生效
2.　cursor.execute(),cursor.executemany(),会返回受影响的行数
3.　cursor.execute(sql,["a","b"])　　列表也可为元组
    传入sql和对应参数
    对应参数
        %s 个数参数的列表,
        %(name)s,也可使用名字为字典进行对应
4.　cursor.executemany(sql,[('egon','sb'),('laoyao','BS')])
        一次传入多组参数，

```python
import pymysql
conn = pymysql.connect(host="localhost", user='root', password='123456', database="zhang")
cursor = conn.cursor()
sql = "insert into userinfo(username,password) values('root','123123')"
#受影响的行数
r = cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
```


## 查询
```python
import pymysql
conn = pymysql.connect(host="localhost", user='root', password='123456', database="zhang")
cursor = conn.cursor()
sql = ""
cursor.execute(sql) #　可只使用sql,不传入参数
cursor.execute(sql,(user,pwd))　# 传入sql和参数
result = cursor.fetchone()#获取sql执行结果的第一个值，再次执行则获取第二个值,如果把获取到的值获取完，再执行则会获取到None
result = cursor.fetchmany(4)#获取sql执行结果的前4个值,如果4大于所有结果的长度，则获取所有的结果
result = cursor.fetchall()#获取sql执行得到的结果的所有值
cursor.scroll(-1, mode='relative') # 相对于当前行进行移动，本行为0，如向上移动一行为-1,向下移动两行为2
cursor.scroll(0,mode='absolute') # 相对与第一行进行移动,0为移动到第一行，因为只能向下移动只能为0或正数
#查询不用commit()
cursor.close()
conn.close()
```