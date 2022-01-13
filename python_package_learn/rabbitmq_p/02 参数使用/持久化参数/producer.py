### 生产者


import pika

# 连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 创建可持久化队列
# queue为队列名称
# durable 创建可持续化队列,创建可持久化要为一个新的队列,不能使用已有的队列

channel.queue_declare(queue='hello3', durable=True)
# 向指定队列插入数据
# exchange 选择路由名称,简单模式直接为空
# routing_key 队列名称
# body 插入的数据
channel.basic_publish(exchange='',
                      routing_key='hello3',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 发送的可持久化保存
                      )
                      )

print(" [x] Sent 'Hello World!'")
