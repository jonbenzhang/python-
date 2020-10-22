import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# 声明交换机,如果交换机已经存在则不执行
channel.exchange_declare(exchange='logs4',
                         exchange_type='topic'
                         )
# 创建队列
# queue 为空,则自动分配一个随机的名字
result = channel.queue_declare("", exclusive=True)
# 获取分配的队列名
queue_name = result.method.queue
print(queue_name)
# 将创建的队列绑定到交换机
# routing_key 绑定关键字,绑定多个关键字则使用多个queue_bind,可用for循环
# '#'代表一个或多个词,'*'代表一个词
channel.queue_bind(exchange='logs4',
                   queue=queue_name,
                   routing_key="USA.#"  # 匹配接受USA的所有信息
                   )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
