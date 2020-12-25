-- args 中的默认参数
--[[
png: 1
har: 1
html: 1
engine: "webkit"
html5_media: false
http2: false
http_method: "GET"
images: 1
load_args: Object
lua_source: "function main(splash, args)\r\n return args\r\nend"
render_all: false
request_body: false
resource_timeout: 0
response_body: false
save_args: Array[0]
timeout: 90
uid: 140157726378864
url: "http://google.com"
viewport: "1024x768"
wait: 0.5
]]
function main(splash, args)
    -- args 就是splash.args
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

