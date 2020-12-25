table_name :要查的表的表名
database_name:要查的数据库名
查看一张表的结构
describe table_name
```
#使用mysql测试
字段名　字段类型　　　是否可为空 额外信息字段 主键 默认值
org_code	varchar(50)	NO	PRI		
event_no	varchar(128)	NO	PRI		
report_form_no	varchar(128)	NO	PRI		
serial_no	varchar(128)	NO	PRI		
last_update_dtime	datetime	YES			
image	blob	YES			
```
#第一种mysql不支持
返回结果和上面类似
1.　show columns from table_name from database_name
2.　show columns from database_name.table_name