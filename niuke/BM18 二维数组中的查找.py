# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM18 二维数组中的查找.py
# @Date    : 2022/07/10:9:25
# @Author  : jinwenlong@oppo.com
"""
    描述
    在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    [
    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
    ]
    给定 target = 7，返回 true。

    给定 target = 3，返回 false。

    数据范围：矩阵的长宽满足 0 \le n,m \le 5000≤n,m≤500 ， 矩阵中的值满足 0 \le val \le 10^90≤val≤10
    9

    进阶：空间复杂度 O(1)O(1) ，时间复杂度 O(n+m)O(n+m)

"""
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