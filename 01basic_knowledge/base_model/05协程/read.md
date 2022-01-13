
# 协程
* 协程本质上是一个线程,不同协程就是在一个线程上切换,但是(threading.current_thread()不同为了方便使用，这是虚假的)
* 协程之间进行切换消耗的时间远远小于线程之间的切换 
* 协程用来规避io操作，来节省时间
* 进程和线程由操作系统控制定时进行切换，协程遇到io(协程能够识别的io)操作才会进行切换,如果没有io则会线性执行
# 并发数
一个4cpu的机器
* 一般最多开5个进程
* 一个进程最多开20个线程
* 一个线程最多开500个协程


一个4cpu的机器，最多开5*20*500个并发

进程　线程　协程
5    20    500


asyncio 在python3.4以后进行支持
遇到io阻塞自动切换，可以自动识别io


async 和await　在python3.5后进行支持
@asyncio.coroutine　换为async
@yield from　换为await


## 阅读
    视频　https://www.bilibili.com/video/BV1Ke411W71L?p=3&spm_id_from=pageDriver
    
    笔记 https://pythonav.com/wiki/detail/6/91/
