import os

pid = os.fork()  # 这里将会创建一个子进程，返回值会是子进程PID值。
print('父子进程都会输出。', pid)  # 这里没有判断语句，将会运行两次，一次是父进程，一次是子进程。
if pid > 0:  # 判断，父进程的返回值会大于0。
    print('子进程的PID是%d,父进程的PID是%d' % (os.getpid(), os.getppid()))  # getpid的获取当前进程的pid,如果子进程getpid的时候，会得到子进程的值，再子进程使用getppid的时候能够获取到父进程的pid。
else:  # 子进程的返回值则会永远是0
    print('父进程的PID是%d' % os.getpid(),os.getppid())  # 当父进程使用getpid的时候获得的是父进程的pid
