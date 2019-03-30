# -*- coding: utf-8 -*-

"""
字符串格式化
"""
from inspect import isgenerator
from typing import Iterable


def fab(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        print(b)
        a, b = b, a + b
        n = n + 1


def test_fun():
    # 斐波那契数列 使用 yield(生成器generator)

    base_url = 'http://image.so.com/zj?ch=art&sn=%d&listtype=new&temp=1'
    start_index = 631
    print("******************")
    print((base_url % start_index))

    # fab 和fab(6) 区别，fab是一个generator functiaon 而fab(6)是调用fab返回的一个generator
    print(isgenerator(fab(6)))
    print(isgenerator(fab))
    print(isinstance(fab(6), Iterable))


if __name__ == '__main__':
    test_fun()
