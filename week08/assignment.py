#!/usr/bin/env python
# encoding: utf-8

import time
from collections.abc import Iterable


'''
list tuple str dict collections.deque
扁平序列: str
不可变序列: tuple str
'''


# @timer 装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.process_time_ns()
        r = func(*args, **kwargs)
        end = time.process_time_ns()
        print(f'{func.__name__} 耗时: {format((end-start), ",")} ns')
        return r
    return wrapper


# 自定义map()
@timer
def mymap(func, iterable):
    if not isinstance(iterable, Iterable):
        print(f"'{type(iterable).__name__}' object is not iterable")
    else:
        for i in iterable:
            yield func(i)

map = timer(map)

if __name__ == '__main__':
    mymap(lambda x: x**2, 1)
    list(mymap(list, 'geektime'*1000000))
    list(map(list, 'geektime'*1000000))

