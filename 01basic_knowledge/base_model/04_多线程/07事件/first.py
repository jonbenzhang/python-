from threading import Event

# 当e.is_set()为false会使程序运行到e.wait()阻塞
# 当e.is_set()为True，程序运行到e.wait()不会阻塞

e = Event()
print(e.is_set())
print("aa")
# 停止阻塞
e.set()
print(e.is_set())
print("bb")
# 开启阻塞
e.clear()
print(e.is_set())
print("cc")
# 当e.is_set()为False时阻塞
e.wait()
print("dd")