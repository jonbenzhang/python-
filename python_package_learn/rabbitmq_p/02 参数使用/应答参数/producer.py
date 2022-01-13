### 生产者


import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 创建队列
# queue为队列名称
channel.queue_declare(queue='hello')
# 向指定队列插入数据
# exchange 选择路由名称,简单模式直接为空
# routing_key 队列名称
# body 插入的数据
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
