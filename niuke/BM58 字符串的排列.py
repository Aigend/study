# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM58 字符串的排列.py
# @Date    : 2022/09/05:22:41
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
from collections import Counter
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        num = list(str)
        result = []

        def trackback(track, counter):
            if len(track) == len(num):
                result.append("".join(track))
            for n in counter:
                if counter[n]:
                    track.append(n)
                    counter[n] -= 1
                    trackback(track, counter)
                    track.pop()
                    counter[n] += 1

        trackback([], Counter(num))
        return result