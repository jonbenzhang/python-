import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pymysql
import psycopg2
from sqlalchemy.pool import NullPool
import sys
from sqlalchemy.dialects.mysql import types

sys.path.append("..")

TABLE_NAME = None
DB_NAME = "pallas_db"
DB_TYPE = "pg"


def mysql_conn():
    host = "10.20.1.24"
    port = "3307"
    database = "testdb"
    username = "sguser"
    passwd = "python1python"
    # 张北现场的大数据库118张表是全的
    # host = "36.133.54.209"
    # port = "10114"
    # database = "zbyl"
    # username = "sguser"
    # passwd = "wGNk1P9HS8AbpfA71BL"
    return pymysql.connect(host=host,
                           port=int(port),
                           user=username,
                           passwd=passwd,
                           db=database
                           )


def pg_conn():
    host = "192.168.2.174"
    passwd = "Zstvgcs@9102"
    return psycopg2.connect(database=DB_NAME, user="postgres", password=passwd, host=host, port="7432")


engine = None
conn = None
if DB_TYPE == "pg":
    conn = pg_conn()
    engine = create_engine('postgresql+psycopg2://', creator=pg_conn,
                           poolclass=NullPool  # 不使用sqlachemy的连接池
                           )
elif DB_TYPE == "mysql":
    conn = mysql_conn()
    engine = create_engine('mysql+pymysql://', creator=mysql_conn,
                           poolclass=NullPool  # 不使用sqlachemy的连接池
                           )


def get_db_names():
    inspector = sqlalchemy.inspect(engine)
    db_names = inspector.get_schema_names()
    return db_names


def get_table_names(db_name=None):
    inspector = sqlalchemy.inspect(engine)

    if DB_TYPE == "pg":
        schema = "public"
        with inspector._operation_context() as conn:
            result = conn.execute(
                sqlalchemy.sql.text(
                    "SELECT c.relname FROM pg_class c "
                    "JOIN pg_namespace n ON n.oid = c.relnamespace "
                    "WHERE n.nspname = :schema AND c.relkind in ('r', 'p')"
                    "AND  NOT EXISTS (SELECT 1 FROM pg_inherits AS i WHERE i.inhrelid = c.oid);"
                ).columns(relname=sqlalchemy.sql.sqltypes.Unicode),
                dict(
                    schema=schema
                ),
            )
            return [name for name, in result]

    table_names = inspector.get_table_names(db_name)
    return table_names


def get_columns(table_name, db_name=None):
    inspector = sqlalchemy.inspect(engine)
    columns = inspector.get_columns(table_name, db_name)
    return columns


def table_info():
    c_dict = {}
    from sqlalchemy.engine import reflection
    inspector = reflection.Inspector.from_engine(engine)
    columns = inspector.get_columns(TABLE_NAME, DB_NAME)
    for i in columns:
        c_dict[i["comment"]] = i["name"]
    print(c_dict)
    return columns


def get_type(field_type):
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
    if any(map(judje_type, types_double)) or any(map(judje_type, types_string)) or any(
            map(judje_type, types_timestamp)):
        return "string"
    return "string"


def tables_info_t():
    c_dict = {}
    from sqlalchemy.engine import reflection
    inspector = reflection.Inspector.from_engine(engine)
    for table in inspector.get_table_names():
        # columns = inspector.get_primary_keys(table, "zbyl_db_linshi_for_add_primary_key_20201008")
        # print("""'%s': {'yes': %s, 'no': []},""" % (table, columns))
        y = inspector.get_table_options(table, "testdb")
        # print("'%s':'%s'," % (table, y['mysql_comment']))
        for i in y:
            print(i)
        # {'baseinfo': {"yes": ['org_code', 'patient_id', 'card_no'], "no": []}},


if __name__ == '__main__':
    # print(get_db_names())
    table_names = get_table_names()
    table_names = [table_name for table_name in table_names if table_name != str.lower(table_name)]
    with open("a.sql","w") as f:
        for table_name in table_names:
            # sql = f''' alter table "{table_name}" add column create_time_ts bigint not null default (extract(epoch from now()) * 1000);\n'''
            # sql = f'''{table_name},'''
            sql = f'''CREATE INDEX {table_name}_create_time_ts ON "{table_name}"("create_time_ts");\n'''
            f.write(sql)
    print(table_names)
    print(len(table_names))
    # tables_info_t()
    # sys.exit()
    # b = table_info()
    # print(b[0])
    # for i in b:
    #     print(i["name"], i["comment"], i["type"])
    # d = [type(i["type"]) for i in b]
    # c = set(d)
    # print(c)
    # excel = excel_write2("first", "first", )
    # excel.write(["字段名", "字段类型", "字段说明", "字段备注"])
    # for i in b:
    #     j = [i["name"], get_type(i["type"]), i["comment"], ""]
    #     print(j)
    #     excel.write(j)
    # excel.save()
