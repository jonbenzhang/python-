import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明交换机
# exchange 交换机名称
# exchange_type 交换机类型:
#   fanout:发布订阅模式
#   direct:关键字模式
#   topic:通配符模式
channel.exchange_declare(exchange='logs4',
                         exchange_type='topic'
                         )

message = "美国的新闻"
# exchange 指定logs交换机,向logs交换机插入数据
# routing_key指定插入信息的关键字
channel.basic_publish(exchange='logs4',
                      routing_key='UK.news',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
