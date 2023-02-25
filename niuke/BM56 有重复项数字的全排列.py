# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM56 有重复项数字的全排列.py
# @Date    : 2022/09/05:21:29
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from copy import copy
from collections import Counter


class Solution:
    def permuteUnique(self, num):
        # write code here
        result = []

        def trackback(track, counter):
            if len(track) == len(num):
                result.append(copy(track))
            for n in counter:
                if counter[n]:
                    track.append(n)
                    counter[n] -= 1
                    trackback(track, counter)
                    track.pop()
                    counter[n] += 1

        trackback([], Counter(num))
        return result


print(Solution().permuteUnique([1, 1, 2]))
