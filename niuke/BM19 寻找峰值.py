# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM19 寻找峰值.py
# @Date    : 2022/07/12:23:07
# @Author  : jinwenlong@oppo.com
"""
给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
2.假设 nums[-1] = nums[n] = -\infty−∞
3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
4.你可以使用O(logN)的时间复杂度实现此问题吗？
"""
# 这道题利用两边为无穷小

from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        # write code here
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            # // 右边是往下，不一定有坡峰
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1 # //右边是往上，一定能找到波峰
        return right