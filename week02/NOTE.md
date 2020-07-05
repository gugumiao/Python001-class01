学习笔记

下载中间件

process_request(request, spider)
Request对象经过下载中间件时会被调用 优先级高的先调用

process_response(request, response, spider)
Resposne对象经过下载中间件时会被调用 优先级高的后调用

process_exception(request, exception, spider)
当process_exception()和process_request()抛出异常会被调用

from_crawler(cls, crawler)
使用crawler创建中间件对象, 并(必须)返回一个中间件对象

