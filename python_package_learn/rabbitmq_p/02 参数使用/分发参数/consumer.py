### 消费者

import pika, time

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 如果生产者没有创建hello4队列,则进行创建hello4队列,
# 如果生产者已创建hello4队列,则不执行
channel.queue_declare(queue='hello4')


# 回调函数
# body为队列中拿到的数据
def callback(ch, method, properties, body):
    time.sleep(4)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动应答


# 没有下面这一行代码则进行轮训分发,不管处理快慢,按顺序一人一个
# 加入下面一行代码进行,公平分发,谁处理完分发给谁
channel.basic_qos(prefetch_count=1)
# 确定监听参数
# queue 队列名称
# auto_ack 应答"参数
# on_message_callback回调函数
channel.basic_consume(queue='hello4',
                      auto_ack=False,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 正式开启监听
channel.start_consuming()
