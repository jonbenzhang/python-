[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/seven-007/)

# [骑猪走秀](https://www.cnblogs.com/seven-007/)

##

  * [ 博客园](https://www.cnblogs.com/)
  * [ 首页](https://www.cnblogs.com/seven-007/)
  * [ 新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
  * [ 联系](https://msg.cnblogs.com/send/%E9%AA%91%E7%8C%AA%E8%B5%B0%E7%A7%80)
  * [ 订阅](javascript:void\(0\))
  * [ 管理](https://i.cnblogs.com/)

随笔 - 119  文章 - 10  评论 - 2

#  [ python之路_常用模块介绍 ](https://www.cnblogs.com/seven-007/p/7512072.html)

一、collections模块

在内置数据类型的基础上(list tuple set dict str)，collections模块提供了如下几种额外的数据类型：namedtuple
deque Counter OrderDict defaultdict

1、namedtuple：生成可以使用名字访问元素的元组，正常的元组可以通过索引进行取值，但是很难看出元组元素所表示的意义，这就是namedtuple数据类型存在的意义。其用法如下实例：

    
    
    from collections import namedtuple
    circle = namedtuple('P',['x','y','r'])      #P可以取任意变量名，无实际用处，但不可或缺
    c1 =circle(2,3,5)
    print(c1.x)
    print(c1.y)
    print(c1.r)

2、deque：list可以高效的进行元素查找，但是对于追加和删除元素比较困难，尤其对于列表较大时，主要是因为列表为单向序列，遵循先进先出原则，只能在列表末尾进行元素的追加（append（））和删除（pop（））。而deque就是为了高效解决列表的增加和删除元素的，除了具有append（）和pop（）外，还具有appendleft（）和popleft（）方法，可以在列表的头部进行元素的增加和删除。

    
    
    from collections import deque
    q = deque(['a','b','c'])
    q.append('x')
    q.appendleft('y')
    print(q)                                #输出结果为：deque(['y', 'a', 'b', 'c', 'x'])
    q.pop()
    print(q)                                #输出结果为：deque(['y', 'a', 'b', 'c'])
    q.popleft()
    print(q)                                #输出结果为：deque(['a', 'b', 'c'])

3、Counter：主要用来跟踪值出现的次数，返回无序的数据类型，用字典键值对进行记录结果，其中元素为key，次数为value。

    
    
    from collections import Counter
    c = Counter('abcdeabcdabcaba')
    print(c)                               #输出结果为：Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

4、OrderDict：使用dict时，key是无序的，无法对其进行迭代，而OrderDict可以使得其变成有序，key的顺序为插入时的顺序，非key本身的顺序。

    
    
    from collections import OrderedDict
    d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])     #可以为这样的形式： d = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    for key in d:
        print(key)                                      #输出结果为：a b c
    d['key'] = 'value'                                  #按照顺序添加在后面
    print(d)                                            #输出结果为：OrderedDict([('a', 1), ('b', 2), ('c', 3), ('key', 'value')])

5、Defaultdict:使用dict时，当key不存在，则会返回keyerror，若希望出现此情况时返回默认值则可用defaultdict。

实例：

`有如下值集合
[``11``,``22``,``33``,``44``,``55``,``66``,``77``,``88``,``99``,``90``]，将所有大于
``66` `的值保存至字典的第一个key中，将小于 ``66` `的值保存至第二个key的值中。``即： {``'k1'``: 大于``66` `,
``'k2'``: 小于``66``}`

    
    
    #常规dict做法
    lst= [11,22,33,44,55,66,77,88,99,90]
    result={}
    for value in lst:
        if value>66:
            if 'k1' in result:
                result['k1'].append(value)
            else:
                result['k1']=[value]
        if value<66:
            if 'k2' in result:
                result['k2'].append(value)
            else:
                result['k2']=[value]
    print(result)
    
    
    #default方法
    from collections import defaultdict
    lst= [11,22,33,44,55,66,77,88,99,90]
    result=defaultdict(list)
    for value in lst:
        if value>66:
            result['k1'].append(value)
        if value<66:
            result['k2'].append(value)
    print(result)                          #输出结果为：defaultdict(<class 'list'>, {'k2': [11, 22, 33, 44, 55], 'k1': [77, 88, 99, 90]})

二、random模块

1、random.random()：返回大于0小于1的随机小数

    
    
    import random
    print(random.random())

2、random.uniform(n,m)：返回大于n小于m的随机小数

    
    
    import random
    print(random.uniform(2,3))

3、random.randint(n,m):返回大于等于n小于等于m的随机整数

    
    
    import random
    print(random.randint(1,5))

4、random.randrange(n,m,2)：返回大于等于n，小于m的随机奇数

    
    
    import random
    print(random.randrange(1,10,2))

5、random.choice(列表等可迭代对象)：随机返回一个元素

    
    
    import random
    print(random.choice([1,10,2]))
    print(random.choice((1,10,2)))
    print(random.choice(range(10)))

6、random.sample(列表等可迭代对象，n)：随机返回n个元素

    
    
    import random
    print(random.sample([1,10,2],2))  #返回一个列表

7、random.shuffle(list)：打乱列表的顺序

    
    
    import random
    val=[1,3,5,7,9]
    random.shuffle(val)
    print(val)

 生成包括数字及大小写字母随机验证码：

    
    
    import random
    def func(n):
        ret=''
        for i in range(n):
            num=random.randint(0,9)
            alpha=chr(random.randint(97,122))
            Alpha = chr(random.randint(65, 90))
            val=random.choice([str(num),alpha,Alpha])
            ret+=val
        return ret
    print(func(6))

三、时间time模块

![](https://images2017.cnblogs.com/blog/1202599/201709/1202599-20170912222239657-300516348.png)

在python中常见三种表示时间的方法为：时间戳、时间元组（结构化时间）、格式化的时间字符串

1、时间戳（timestamp)：通常来说，时间戳表示从1970年1月1日0时0分0秒开始时间的偏移量，单位为秒。

获取时间戳的方法：

    
    
    #（1）time.time()方式获取当前时间戳
    import time
    print(time.time())
    
    #（2）利用time.mktime(结构化时间)转化
    import time
    time_tuple = time.localtime(1500000000)#结构化时间
    print(time.mktime(time_tuple))

2、格式化的时间的字符串（format string)：

**格式化字符** | **意义说明** | **格式化字符** | **意义说明**  
---|---|---|---  
%Y |四位数的年份表示（000-9999）| %B | 本地完整的月份名称 
%y |两位位数的年份表示（00-99） | %c |本地相应的日期表示和时间表示  
%m | 月份（01-12）| %j |年内的一天（001-366）  
%d |月内中的一天（0-31）| %P |本地A.M.或P.M.的等价符  
%H |24小时制小时数（0-23）| %U |一年中的星期数（00-53）星期天为星期的开始  
%I |12小时制小时数（01-12）| %w |星期（0-6），星期天为星期的开始  
%M |分钟数（00=59）| %W |一年中的星期数（00-53）星期一为星期的开始  
%S | 秒（00-59）| %x |本地相应的日期表示  
%a |本地简化星期名称| %X |本地相应的时间表示  
%A | 本地完整星期名称| %Z |当前时区的名称  
%b |本地简化的月份名称| %% |%号本身  
  
获取格式化时间字符串：

    
    
    #time.strftime("格式定义","结构化时间")  结构化时间参数若不传，则显示当前时间
    import time
    print(time.strftime("%Y-%m-%d %X"))                                    #输出结果：2017-09-12 23:21:34
    print(time.strftime("%Y-%m-%d",time.localtime(1500000000)))            #输出结果：2017-07-14



3、时间元组(time_structrue)：struct_time元组共有9个元素，分别为：年，月，日，时，分，秒，一年中第几周，一年中第几天等。

索引（Index）| 属性（Attribute）| 值（Values）  
---|---|---  
0 | tm_year（年） | 比如2011  
1 | tm_mon（月） | 1 - 12  
2 | tm_mday（日） | 1 - 31  
3 | tm_hour（时） | 0 - 23  
4 | tm_min（分） | 0 - 59  
5 | tm_sec（秒） | 0 - 61  
6 | tm_wday（weekday） | 0 - 6（0表示周日）  
7 | tm_yday（一年中的第几天） | 1 - 366  
8 | tm_isdst（是否是夏令时） | 默认为-1  
  
获取结构化时间：

（1）利用time.localtime()或者time.gmtimei()从时间戳转换

    
    
    #time.gmtime(时间戳) UTC时间，与英国伦敦当地时间一致
    import time
    print(time.gmtime(1500000000))  
    #输出结果：time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=2, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)
    
    
    #time.localtime(时间戳) 当地时间，例如我们现在在北京执行这个方法：与UTC时间相差8小时，UTC时间+8小时 = 北京时间
    import time
    print(time.localtime(1500000000))
    #输出结果为：time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=10, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)

（2）利用time.strptime()从格式化时间的字符串转换

    
    
    #time.strptime(时间字符串,字符串对应格式)
    import time
    print(time.strptime("2017-03-16","%Y-%m-%d"))
    #输出结果为：time.struct_time(tm_year=2017, tm_mon=3, tm_mday=16, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=75, tm_isdst=-1)
    print(time.strptime("07/24/2017","%m/%d/%Y"))
    #输出结果为：time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=205, tm_isdst=-1)

 4、补充：获取如下格式化时间字符串的方法

![](https://images2017.cnblogs.com/blog/1202599/201709/1202599-20170913113228172-1604429513.png)

（1）通过结构化时间：time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串。

    
    
    import time
    print(time.asctime(time.localtime(1500000000)))   #输出结果为：'Fri Jul 14 10:40:00 2017'
    print(time.asctime())                             #输出结果为：'Mon Jul 24 15:18:33 2017'

（2）通过时间戳时间：time.ctime(时间戳) 如果不传参数，直接返回当前时间的格式化串。

    
    
    import time
    print(time.ctime(1500000000))                     #输出结果为：'Fri Jul 14 10:40:00 2017'
    print(time.ctime())                               #输出结果为：Wed Sep 13 11:41:59 2017

例题：计算2008年8月8日20点30分到2017年10月1日06点过去了多少年多少月多少天多少小时多少分

    
    
    import time
    time_last=time.mktime(time.strptime('2008-08-08 20:30:00','%Y-%m-%d %H:%M:%S'))
    time_now=time.mktime(time.strptime('2017-10-01 06:00:00','%Y-%m-%d %H:%M:%S'))
    dif_time=time_now-time_last
    time_struct=time.gmtime(dif_time)
    print(time_struct)
    print('2008年8月8日20点30分到2017年10月1日06点过去了%s年%s月%s天%s小时%s分%s秒'  
    %(time_struct.tm_year-1970,time_struct.tm_mon-1,time_struct.tm_mday-1,time_struct.tm_hour,time_struct.tm_min,time_struct.tm_sec))

四、os模块

os模块是与操作系统交互的一个接口

    
    
    '''
    os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
    os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
    os.curdir  返回当前目录: ('.')
    os.pardir  获取当前目录的父目录字符串名：('..')
    os.makedirs('dirname1/dirname2')    可生成多层递归目录
    os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
    os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
    os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
    os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
    os.remove()  删除一个文件
    os.rename("oldname","newname")  重命名文件/目录
    os.stat('path/filename')  获取文件/目录信息
    os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
    os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
    os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
    os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
    os.system("bash command")  运行shell命令，直接显示
    os.popen("bash command)  运行shell命令，获取执行结果
    os.environ  获取系统环境变量
    
    
    os.path
    os.path.abspath(path) 返回path规范化的绝对路径 os.path.split(path) 将path分割成目录和文件名二元组返回 os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
                            即os.path.split(path)的第二个元素
    os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
    os.path.isabs(path)  如果path是绝对路径，返回True
    os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
    os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
    os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
    os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
    os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
    os.path.getsize(path) 返回path的大小
    '''

注意：os.stat('path/filename')  获取文件/目录信息 的结构说明

    
    
    '''
    stat 结构:
    
    st_mode: inode 保护模式
    st_ino: inode 节点号。
    st_dev: inode 驻留的设备。
    st_nlink: inode 的链接数。
    st_uid: 所有者的用户ID。
    st_gid: 所有者的组ID。
    st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
    st_atime: 上次访问的时间。
    st_mtime: 最后一次修改的时间。
    st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
    '''

五、sys模块

sys模块是python解释器交互的一个接口

    
    
    '''
    sys.argv           命令行参数List，第一个元素是程序本身路径
    sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
    sys.version        获取Python解释程序的版本信息
    sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
    sys.platform       返回操作系统平台名称
    '''

六、序列化模块

序列化的定义：将字典、列表等转化为一个字符串的过程称为称为序列化。序列化的作用：a.以某种存储形式使自定义[对象持久化](https://baike.baidu.com/item/%E5%AF%B9%E8%B1%A1%E6%8C%81%E4%B9%85%E5%8C%96)；b.将对象从一个地方传递到另一个地方；

c.使程序更具维护性

1、json模块：提供了4个功能，分别为：dumps、loads、dump、load

dumps与loads

    
    
    #1、序列化字典实例
    import json
    dic = {'k1':'v1','k2':'v2','k3':'v3'}
    str_dic = json.dumps(dic)                #序列化：将一个字典转换成一个字符串
    print(type(str_dic),str_dic)             #<class 'str'> {"k3": "v3", "k1": "v1", "k2": "v2"}，注意：json转换完的字符串类型的字典中的字符串是由""表示的
    
    
    dic2 = json.loads(str_dic)               #反序列化：将一个字符串格式的字典转换成一个字典 #注意，要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示   
    print(type(dic2),dic2)                   #<class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}  
    #2、序列化列表实例   
    import json   
    list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]   
    str_dic = json.dumps(list_dic)                         #也可以处理嵌套的数据类型   
    print(type(str_dic),str_dic)                           #<class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]   
    list_dic2 = json.loads(str_dic)   
    print(type(list_dic2),list_dic2)                       #<class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]

dump与load

    
    
    import json
    f = open('json_file','w')
    dic = {'k1':'v1','k2':'v2','k3':'v3'}
    json.dump(dic,f)                                      #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
    f.close()  
    
    import json
    f = open('json_file')
    dic2 = json.load(f)                                   #load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
    f.close()
    print(type(dic2),dic2)                                #输出结果：<class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

2、pickle模块：提供了4个功能，分别为：dumps、loads、dump、load
json与pickle的区别：（1）json是用与字符串与python数据类型的转换，但是它是所有语言都可以识别的一种的数据结构，如序列化后存放在文件里可以被java等语言读取；（2）pickle是python特有数据类型与python数据的转换，序列化的文件其他语言读不懂。如果你序列化的内容是列表或者字典，我们非常推荐你使用json模块，但如果出于某种原因你不得不序列化其他的数据类型，而未来你还会用python对这个数据进行反序列化的话，那么就可以使用pickle。

    
    
    import pickle
    dic = {'k1':'v1','k2':'v2','k3':'v3'}
    str_dic = pickle.dumps(dic)
    print(str_dic)       #一串二进制内容
    
    dic2 = pickle.loads(str_dic)
    print(dic2)          #字典
    
    import time
    struct_time  = time.localtime(1000000000)
    print(struct_time)
    f = open('pickle_file','wb')
    pickle.dump(struct_time,f)
    f.close()
    
    f = open('pickle_file','rb')
    struct_time2 = pickle.load(f)
    print(struct_time2.tm_year)

3、shelve模块：只提供了一个open方法，如字典一样通过key进行存入和读取数据

    
    
    import shelve
    f = shelve.open('shelve_file')
    f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}       #直接对文件句柄操作，就可以存入数据
    f.close()
    
    import shelve
    f1 = shelve.open('shelve_file')
    existing = f1['key']                                             #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
    f1.close()
    print(existing)



posted @ 2017-09-12 23:41  [骑猪走秀](https://www.cnblogs.com/seven-007/)  阅读(99)
评论(0)  [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=7512072)
[收藏](javascript:void\(0\))

[刷新评论](javascript:void\(0\);)刷新页面返回顶部

Copyright (C) 2020 骑猪走秀  
Powered by .NET Core on Kubernetes

