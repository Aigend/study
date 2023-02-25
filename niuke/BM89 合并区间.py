# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM89 合并区间.py
# @Date    : 2022/06/28:23:47
# @Author  : jinwenlong@oppo.com
from typing import List


class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

    def __str__(self):
        return str(self.start) + "_" + str(self.end)

    def __repr__(self):
        return str(self.start) + "_" + str(self.end)
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # write code here
        if not intervals:
            return intervals
        result = []
        # 第一种解题思路错误，不应该用x.end排序，应该用x.start排序
        # intervals.sort(key=lambda x: x.end)
        # temp = intervals[0]
        # for i in range(1, len(intervals)):
        #     if intervals[i].start <= temp.end:
        #         # print(i, "**")
        #         temp.end = intervals[i].end
        #         temp.start = min(temp.start, intervals[i].start)
        #         # print(temp)
        #     else:
        #         # print(i, "###")
        #         result.append(temp)
        #         temp = intervals[i]
        #         # print(i, result)
        # 重新变换思路
        # [1,5] [2,3],[4,6]
        intervals.sort(key=lambda x: x.start, reverse=False)
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start > temp.end:
                result.append(temp)
                temp = intervals[i]
            else:
                temp.end = max(temp.end, intervals[i].end)

        result.append(temp)
        # print(result)
        return result


if __name__ == '__main__':
    # Solution().merge([Interval(10,30), Interval(20, 60), Interval(80,100), Interval(150, 180)])

    print(Solution().merge([Interval(2, 3), Interval(1, 4)]))
