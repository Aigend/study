# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM53 缺失的第一个正整数.py
# @Date    : 2022/09/06:21:57
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
"""
    描述
    给定一个未排序的整数数组nums，请你找出其中没有出现的最小的正整数

    进阶： 空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

    数据范围:
    -231<=nums[i]<=231-1
    0<=len(nums)<=5*105
    输入：
        [-2,3,4,1,5]
        返回值：2
"""
class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here
        # n = len(nums)
        # mp = dict()
        # # 哈希表记录数组中出现的每个数字
        # for i in range(n):
        #     if nums[i] in mp:
        #         mp[nums[i]] += 1
        #     else:
        #         mp[nums[i]] = 1
        # res = 1
        # # 从1开始找到哈希表中第一个没有出现的正整数
        # while res in mp:
        #     res += 1
        # return res

        mp = set(nums)
        res = 1
        # 从1开始找到哈希表中第一个没有出现的正整数
        while res in mp:
            res += 1
        return res