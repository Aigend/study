# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM21 旋转数组的最小数字.py
# @Date    : 2022/07/12:23:27
# @Author  : jinwenlong@oppo.com
"""
描述
有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。

数据范围：1 \le n \le 100001≤n≤10000，数组中任意元素的值: 0 \le val \le 100000≤val≤10000
要求：空间复杂度：O(1)O(1) ，时间复杂度：O(logn)O(logn)
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param rotateArray int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
        # write code here
        left = 0
        right = len(rotateArray) - 1
        while left < right:
            mid = (left+right)//2
            if rotateArray[mid] <rotateArray[right]:
                right = mid
            elif rotateArray[mid] == rotateArray[right]:
                right -= 1
            elif rotateArray[mid] > rotateArray[right]:
                left = mid + 1
        return rotateArray[left]


        #     print(rotateArray[left])
        #     print(rotateArray[mid])
        #     print(rotateArray[right])
        #     print(mid)
        #     print("###")
        #     if rotateArray[mid] > rotateArray[left]:
        #         print("&&&")
        #         left = mid
        #     elif rotateArray[mid] == rotateArray[left]:
        #         print("^^^")
        #         left+=1
        #     else:
        #         print("()(")
        #         right = mid
        # print("***")
        # print(left)
        # print(right)
        # print(rotateArray[left])
        # print(rotateArray[right])
        # return min(rotateArray[left], rotateArray[left])

print(Solution().minNumberInRotateArray([1,0,1,1,1]))
