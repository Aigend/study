# !/user/bin/env python
# -*- coding:utf-8 -*-
# @project: PyCharm
# @Author: wenlong.jin
# @Time: 2023/3/17 20:33
# @File: py_gevent.py
import time

import gevent
from gevent import monkey
monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

print("********")
g1 = gevent.spawn(f1, 5)
print("------")
g2 = gevent.spawn(f2, 5)
print("#####")
g3 = gevent.spawn(f3, 5)
print("&&&")
print("^^^^^")
g1.join()
gevent.sleep(10)
print("@@@")
g2.join()
print("%%%")
g3.join()

# gevent.joinall([g1,g2, g3])

print("******************")

import gevent
from gevent import monkey
import urllib.request
monkey.patch_all()


def downloader(file_name, url_address):
    req = urllib.request.urlopen(url_address)
    content = req.read()
    with open(file_name, "wb") as f:
        f.write(content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "绝地求生女解说Corrine宅个人Vlog视频.mp4",
                                 "https://img.dongyoutu.com/20210423/841dd2e192db6c70630ba12112c386f8.mp4"),
        gevent.spawn(downloader, "《跑跑卡丁车：RUSH+》与《绝地求生Mobile》一起联手推出搞笑视频.mp4", "https://img.dongyoutu.com/20210402/1111.mp4")
                    ])


if __name__ == '__main__':
    main()
    
# https://blog.csdn.net/weixin_43988680/article/details/123903473 
# 元类的介绍
# !/user/bin/env python
# -*- coding:utf-8 -*-
# @project: PyCharm
# @Author: wenlong.jin
# @Time: 2023/3/17 21:46
# @File: py_type.py
class MyMeta(type):

    def __new__(cls, *args, **kwargs):
        print("mymeta __new__ ...")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, class_name, class_bases, class_dic):
        print("mymeta __init__ ...")
        print(self)
        print(class_bases)
        print(self.__bases__)
        print(class_dic)
        if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')


    # def __call__(self, *args, **kwargs):
    #     print("mymeta __call__ ...")


class People(metaclass=MyMeta):
    """

    """
    def __new__(cls, *args, **kwargs):
        print("people __new__ ...")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("people __init__ ...")

    def __call__(self, *args, **kwargs):
        print("people __call__ ...")
