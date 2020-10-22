### 消费者

import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 如果生产者没有创建hello3队列,则进行创建hello3队列,
# 如果生产者已创建hello3队列,则不执行
channel.queue_declare(queue='hello3', durable=True)


# 回调函数
# body为队列中拿到的数据
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 确定监听参数
# queue 队列名称
# auto_ack 应答"参数
# on_message_callback回调函数
channel.basic_consume(queue='hello3',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式开启监听
channel.start_consuming()
