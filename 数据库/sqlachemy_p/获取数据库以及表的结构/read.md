### 创建一个reflection
from sqlalchemy.engine import reflection
inspector = reflection.Inspector.from_engine(engine)
### 获取所有的数据库
inspector.get_schema_names()
### 获取数据库中的所有表
inspector.get_table_names(table_name)
* table_name 为表名
### 获取数据库表中的结构
inspector.get_columns(table_name, database_name)
* table_name 表名
* database_name 数据库名
### 获取数据库表中的主键字段
inspector.get_primary_keys(table_name, database_name)
* table_name 表名
* database_name 数据库名