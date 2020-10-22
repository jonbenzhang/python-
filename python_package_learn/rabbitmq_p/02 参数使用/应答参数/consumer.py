### 消费者

import pika
import time

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 如果生产者没有创建hello队列,则进行创建hello队列,
# 如果生产者已创建hello队列,则不执行
channel.queue_declare(queue='hello')


# 回调函数
# body为队列中拿到的数据
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动应答


# 确定监听参数
# auto_ack 应答参数默认True,自动应答,接受后自动删除,
# auto_ack 应答参数默认False,手动应答,为在回调函数中进行应答
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式开启监听
channel.start_consuming()
