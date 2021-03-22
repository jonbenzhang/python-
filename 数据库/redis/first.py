import redis


def redis_connect():
    """
    创建redis连接池
    :return:
    """
    # 方式1和方式2创建的都是redis的连接池，返回的结果相同只是调用方式不同
    # 方式1
    # password :如有密码添加参数password
    # 参数都会被传递到redis.Redis对象中，需要不知道的参数可以去redis.Redis中去找
    pool = redis.ConnectionPool(host='172.20.3.29', port=6380, db=0, decode_responses=True)
    r1 = redis.Redis(connection_pool=pool)
    # 方式2
    # decode_responses=True 执行写入的数据是字符串格式,否则会存储为二进制
    # 如有密码url 为redis://密码@172.20.3.29:6380/0
    r2 = redis.from_url("redis://172.20.3.29:6380/0", decode_responses=True)
    return r1


r = redis_connect()


#
#

def redis_u():
    """
    直接调用链接池执行命令
    :return:
    """
    r.set('foo', 'Bar')
    print(r.get('foo'))


def pipeline_u():
    # redis pipeline
    """
    pipeline,会把pipeline中的redis命令缓存，当使用execute 时一起传递到redis服务器
    :return:
    """
    pipe = r.pipeline()
    pipe.set("a", 1)  # 命令会先缓存
    print(pipe.get('foo'))
    pipe.set('b', 2)  # 命令会先缓存
    pipe.execute()  # 命令传递到redis执行


def pipeline_transaction():
    """
    pipeline和事务组合使用
    :return:
    """
    with r.pipeline() as pipe:
        while True:
            try:
                pipe.watch("c")  # 开始watch c,直到下一个事务开始然后结束
                # pipe.set("c", 11) # 如果watch后，在事务开启前,修改watch 的key值,会造成watch报错
                c_val = pipe.get("c")
                pipe.multi()  # 开启事务
                pipe.set("c", 2)
                pipe.execute()  # 执行事务
                break
            except redis.WatchError:
                print("error")
                continue


if __name__ == '__main__':
    # print()
    # pipeline_transaction()
    redis_u()
