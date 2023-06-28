# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ3 数组中重复的数字.py
# @Date    : 2022/08/08:21:03
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
from typing import List
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        if not numbers and len(numbers) <2:
            return -1
        s = set()
        for value in numbers:
            if value not in s:
                s.add(value)
            else:
                return value