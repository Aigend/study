# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ4 二维数组中的查找.py
# @Date    : 2022/08/08:21:08
# @Author  : jinwenlong@oppo.com
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        row = len(array)
        col = len(array[0])
        i = row-1
        j = 0
        while i >= 0 and j < col:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                i = i - 1
            elif array[i][j] < target:
                j = j + 1
        return False