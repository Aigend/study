# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM55 没有重复项数字的全排列.py
# @Date    : 2022/09/05:20:09
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from copy import copy
class Solution:
    def permute(self , num):
        # write code here
        result = []
        track = []
        def trackback(track, num, result):
            # result.append("####")
            if len(track) == len(num):
                # print(track)
                result.append(copy(track))
                print(result)
                return
            for i in num:
                if i in track:
                    continue
                track.append(i)
                print(track)
                trackback(track, num, result)
                track.pop()
        trackback(track, num, result)
        return result


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))