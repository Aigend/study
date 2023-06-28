# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : LeetCode-python 496.下一个更大元素 I.py
# @Date    : 2022/07/10:10:16
# @Author  : jinwenlong@oppo.com
# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
#
# 解题思路
# 遍历nums数组，
# 1.当stack为空或者当前元素小于栈顶元素时，该数进栈
# 2.当前元素大于栈顶元素时，栈顶元素出栈，该元素为栈顶元素的下一个更大元素，用字典保存，继续和栈顶元素比较，直到1的情况，进行1的操作
# 3.遍历findNums，找出该元素在字典中对应的值，若不在字典中，用-1代替，存入结果数组

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        dic = {}
        for num in nums:
            while len(st) and st[-1] < num:
                dic[st.pop()] = num
            st.append(num)
        return [dic.get(x, -1) for x in findNums]
