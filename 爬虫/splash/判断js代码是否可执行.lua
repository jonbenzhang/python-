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