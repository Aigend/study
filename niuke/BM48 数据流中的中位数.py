# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM48 数据流中的中位数.py
# @Date    : 2022/09/06:23:00
# @Author  : jinwenlong@oppo.com
class Solution:
    def __init__(self):
        self.val = []
    def Insert(self, num):
        if len(self.val) == 0:
            #val中没有数据，直接加入
            self.val.append(num)
        #val中有数据，需要插入排序
        else:
            i = 0
            #遍历找到插入点
            while i < len(self.val):
                if num <= self.val[i]:
                   break
                i = i + 1
            #插入相应位置
            self.val.insert(i, num)
    def GetMedian(self):
        n = len(self.val)
        #奇数个数字
        if n % 2 == 1:
            #类型转换
            return self.val[n // 2]
        #偶数个数字
        else:
            return (self.val[n // 2] + self.val[n // 2 - 1]) / 2.0
