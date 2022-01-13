import queue
# 创建一个队列的对象
q = queue.Queue(maxsize=10)
q.put(1111)
q.put(2222)
q.put(3333)
print(q.get())
print(q.get())
print(q.get())
# block = False 当没有数可取以后报错
# block = False 当没有数可取以后报错
print(q.get(block=False))
print(q.get(block=False))
