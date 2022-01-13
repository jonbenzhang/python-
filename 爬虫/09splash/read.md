# splash

有的地方不详细，详细查看python3网络爬虫开发实战

splash模拟浏览器的操作

```lua
-- 函数名为main()是固定的
function main(splash,args)
    --访问百度的页面
    splash:go("http://www.baidu.com")
    --等待0.5秒钟
    splash:wait(0.5)
    --使用evaljs()方法传入javaScript脚本，
    --document.titile,是获取网页的标题
	-- local 定义局部变量,没有local则是定义全局变量
    local title = splash:evaljs("document.titile")
    -- 返回
    -- 可以返回字典类型，也可以返回字符串
    return {title=title}
    -- 返回字符串
    return "hello"
end
```

异步处理

```lua
function main(splash, args)
    local example_urls = {"www.baidu.com","www.taobao.com","www.zhihu.com"}
    local urls = args.urls or example_urls
    local results = {}
    for index, url in ipairs(urls) do
        -- ".."等同于python中的加号
        local ok,reason = splash:go("http://"..url)
        -- 如果加载页面出错,ok就会nil
        if ok then
            splash:wait(2)
            -- 获取网页的png图片
            results[url]=splash:png()
        end
    end
--     return args
    return results
end
```

## 配置splash参数
如下面为配置禁止使用js

```lua
--splash
function main(splash,args)
    splash:go("http://www.baidu.com")
    splash:wait(0.5)
    -- 当splash.js_enabled为false时，该页面不可执行js代码
    splash.js_enabled = false
    -- 此处执行js代码会报错，因为上面禁止了js代码的执行呢
    local title = splash:evaljs("document.titile")
    return {title=title}
end
```

splash参数

1. resource_timeout 

  设置超时时间，如果0或者为nil(python中的None),代表不检测超时，超时会抛出如下异常

  ```lua
  function main(splash)
    	splash.resource_timeout =100
   assert(splash:go("http://www.taobao.com"))
   return splash:png()
  end
  ```

  

  ```
  {
      "error": 400,
      "type": "ScriptError",
      "description": "Error happened while executing Lua script",
      "info": {
          "source": "[string \"--splash\r...\"]",
          "line_number": 4,
          "error": "network5",
          "type": "LUA_ERROR",
          "message": "Lua error: [string \"--splash\r...\"]:4: network5"
      }
  }
  ```

2. images_enabled

   设置是否加载图片

   * 默认为true会加载图片,修改为false会禁止加载图片

   * 通过这个属性设置图片是否可加载，节省流量.
   
   * 但是禁用图片可能,会影响js的渲染，因为禁用图片影响了dom高度，从而影响dom节点的位置
   * splash使用缓存，开始加载出来的图片，禁用了图片加载后可能还会显示出来，重启splash即可
   
3.  scoll_position

   控制页面滚动

   splash.scroll_position = {x=100,y=400}　向左移动100px，向下移动400px

   ```lua
   function main(splash)
     	splash.resource_timeout =100
       assert(splash:go("http://www.taobao.com"))
     	splash.scroll_position = {x=100,y=400}
       return splash:png()
   end
   ```

   ## splash 对象方法

   ### go()

   go方法来请求某个连接

   ![image-20200909170208750](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909170208750.png)

   ### wait()

   控制页面的等待时间

   ![image-20200909170329872](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909170329872.png)

   ### jsfun()

   执行自定义的js脚本函数,吧js函数转化为lua函数
   
   ![image-20200909170848807](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909170848807.png)
   
   ###　evaljs()
   
   执行js代码，并获取最后一条js返回的结果

![image-20200909170924853](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909170924853.png

### runjs()

执行js代码，相对与evaljs更加倾向于代码的执行．实现某种动作

![image-20200909171157783](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909171157783.png)

### autoload()

### autoload()

   设置页面访问自动加载的对象

   ![image-20200909171421075](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909171421075.png)

###  call_later()

   定时任务或延时执行

 ###  http_get()

      模拟http的get请求

###  http_post()

​	模拟http的post请求

### set_content()

​	设置页面的内容

### html()

​	获取网页的源代码

### png()

​	获取网页的png截图

### jpeg()

​	获取网页的jpeg截图

### har()

获取网页加载的过程描述

### url()

获取当前正在访问的页面

### get_cookies()

获取当前页面的cookies

### add_cookies()

在当前页面添加cookie

### clear_cookies()

清除当前页面的所有cookies

### get_viewport_size()

获取当前浏览器的宽和高

### set_viewport_size()

设置当前浏览器的页面的大小

### set_viewport_full()

设置浏览全屏显示

### set_user_agent()

设置浏览器的User-Agent

### set_custom_headers()

设置请求头

### select()

　使用css选择器，选择符合条件的节点,如有多个只会返回一个

### select_all()

　使用css选择器，选择符合条件的节点,如有多个,返回所有符合条件的

### mouse_click()

​	模拟鼠标点击

### send_text()

进行数据输入，首先定位到tag标签

input = splash:select("#kw ”)
input:send_text (’ Splash')

## 使用api调用splash

  ### 使用api获取渲染后的html页面代码

​	curl http ://localhost :80SO/render . html?url=https://www.baidu.com

​	可以设置渲染的参数

   如下　设置等待5秒钟

​	url =’ http://localhost :8050/render.html?url=https ://www.taobao.com&wait=5 '

### 使用api获取渲染后的页面的png图片

会返回图片的二进制数据

```shell
curl http ://localhost :80SO/render.png?url=https://www .taobao.com&wait=S&width=1000&height=700
```

![image-20200909175741431](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909175741431.png)

### 使用api获取渲染后的页面的jpeg图片

* 此接口和 render.pug 类似,不过它返回的是 JPEG 格式的图片二进制数据 。
* 另外, 此接口比 render. png 多了参数 quality ,它用来设置罔片质量

### render.har

 获取页面加载的HAR数据

### render.json

包含前面接口的所有功能，只是返回格式为json

需要上面那个功能的数据就把它等于1传入

如下html=1,har=1,会返回网页源代码和har数据

curl http://localhost:8050/render.json?url=https://httpbin.org&html=l&har=l

### execute

可把转化的splash lua,脚本使用quote转化为字符串，通过url传入执行

![image-20200909180523463](/home/zhangmeng/.config/Typora/typora-user-images/image-20200909180523463.png)



