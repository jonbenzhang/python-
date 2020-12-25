from sqlalchemy import create_engine
import pymysql
from sqlalchemy.engine import reflection
from sqlalchemy.pool import NullPool

mysql_host = "10.20.1.24"
mysql_port = 3307
mysql_user = "sguser"
mysql_passwd = "python1python"
mysql_db = "c"


def mysql_conn():
    # mysql_host = cp.get('mysql2', 'host')
    # mysql_port = cp.get('mysql2', 'port')
    # mysql_user = cp.get('mysql2', 'user')
    # mysql_passwd = cp.get('mysql2', 'passwd')
    # mysql_db = cp.get('mysql2', 'db')
    return pymysql.connect(host=mysql_host,
                           port=int(mysql_port),
                           user=mysql_user,
                           passwd=mysql_passwd,
                           db=mysql_db
                           )


engine = create_engine('mysql://', creator=mysql_conn,
                       poolclass=NullPool  # 不使用sqlachemy的连接池
                       )

inspector = reflection.Inspector.from_engine(engine)

# for schema in inspector.get_schema_names():
#     print(schema)


from sqlalchemy.dialects.mysql.types import VARCHAR
from sqlalchemy.dialects.mysql import types


def type_transform(field_type, primary_key_sign):
    # print(type(field_type))
    # 转化为string类型的类型对应
    types_string = [types.VARCHAR, types.CHAR,
                    types.LONGBLOB, types.MEDIUMBLOB, types.TINYBLOB,
                    types.TEXT, types.LONGTEXT, types.MEDIUMTEXT]
    types_timestamp = [types.DATETIME, types.TIME, types.TIMESTAMP]
    types_double = [types.FLOAT, types.DECIMAL, types.DOUBLE]
    types_bigint = [types.BIGINT, types.MEDIUMINT, types.SMALLINT, types.TINYINT]
    from functools import partial
    judje_type = partial(isinstance, field_type)
    if primary_key_sign:
        if any(map(judje_type, types_double)):
            return "string"
    if any(map(judje_type, types_timestamp)):
        return "timestamp"
    if any(map(judje_type, types_bigint)):
        return "bigint"
    if any(map(judje_type, types_string)):
        return "string"
    if any(map(judje_type, types_double)):
        return "double"
    return "string"


def sql_transform(column, primary_key_sign=False):
    # print(column)
    field_type = type_transform(column['type'], primary_key_sign)
    column_data = ""
    if column["comment"]:
        #去除单引号
        column_data = " COMMENT '%s'" % (column["comment"].replace("'", ""))
    column_sql = "`%s` %s %s,\n" % (column["name"], field_type, column_data)
    return column_sql


def create_sql(database_name, table_name):
    sql = "CREATE TABLE `%s` ( \n" % (table_name)
    # 表注释
    table_comment = inspector.get_table_options(table_name, schema=database_name).get("mysql_comment")
    sql_table_comment = ""
    if table_comment:
        sql_table_comment = " COMMENT '%s'" % (table_comment)
    # 获取所有主键的字段
    primary_keys = inspector.get_pk_constraint(table_name, database_name)["constrained_columns"]
    table_data = inspector.get_columns(table_name, database_name)
    table_data_primary_key = [i for i in table_data if i['name'] in primary_keys]
    # 删除主键字段
    list(map(table_data.remove, table_data_primary_key))
    for column in table_data_primary_key:
        sql += sql_transform(column, True)
    for column in table_data:
        sql += sql_transform(column)
    sql_primary_keys = "PRIMARY KEY ("
    sql_primary_keys += ",".join(['`' + i + '`' for i in primary_keys])
    sql_primary_keys += ")\n"
    sql += sql_primary_keys
    sql += ")%s stored as kudu;\n\n" % (sql_table_comment)
    print(sql)
    return sql


def table_name_chinese(table_name):
    """
    判断建表，表名是否有中文
    """
    print(table_name)
    for ch in table_name:
        if u'\u4e00' <= ch <= u'\u9fff':
            return False
    return True


def main():
    with open("./a.sql", "w") as f1:
        for table in inspector.get_table_names(mysql_db):
            print(table)
            if not inspector.get_pk_constraint(table, mysql_db)["constrained_columns"]:
                # 如果没有主键
                continue
            if not table_name_chinese(table):
                # 如果表名为中文
                continue
            sql = create_sql(mysql_db, table)
            f1.write(sql)

if __name__ == '__main__':
    # main()
    # print(len(inspector.get_table_names("c")))
    inspector.g
    # create_sql("gkyy_medical", "baseinfo")
    # x = inspector.get_pk_constraint("baseinfo", "gkyy_medical")
    # x = inspector.get_pk_constraint("d", "a")
    # print(x)
    # a = inspector.get_table_options("baseinfo")
    # print(a)
