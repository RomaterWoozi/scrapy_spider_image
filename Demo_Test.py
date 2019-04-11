# -*- coding: utf-8 -*-


import pymongo
import json

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


# def test_fun():
# 斐波那契数列 使用 yield(生成器generator)

# base_url = 'http://image.so.com/zj?ch=art&sn=%d&listtype=new&temp=1'
# start_index = 631
# print("******************")
# print((base_url % start_index))
#
# # fab 和fab(6) 区别，fab是一个generator functiaon 而fab(6)是调用fab返回的一个generator
# print(isgenerator(fab(6)))
# print(isgenerator(fab))
# print(isinstance(fab(6), Iterable))
# # 创建数据库
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# dblist = myclient.list_database_names()
# imgdb_status = False
# # 判断数据库是否存在
# if "imgdb" in dblist:
#     print("imgdb  exists")
#     imgdb_status = True
#
# if imgdb_status:
#     mydb = myclient['imgdb']
#     # 判断collection是否存在
#     collist = mydb.list_collection_names()
#     if "imgcollection" in collist:
#         print("collection imgcollection exists")
#
# for i in range(5):
#     print(i)

def readjson_file(file_path):
    fo = open(file_path, mode='r+',encoding='UTF-8')
    json_data = fo.read()
    return json.loads(json_data)


if __name__ == '__main__':
    for i in range(-10, -100, -30):
        print(i)

    client = pymongo.MongoClient(host='localhost', port=27017)
    imgdb = client['imgdb']
    imgcollection = imgdb['imgcollection']
    imgcollection.insert_many(readjson_file('ebookspider.json'))
    client.close()
    # test_fun()
