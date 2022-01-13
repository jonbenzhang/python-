import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明交换机
# exchange 交换机名称
# exchange_type 交换机类型:
#   fanout:发布订阅模式
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout'
                         )

message = "test"
# exchange 指定logs交换机,向logs交换机插入数据
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
