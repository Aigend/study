# @File    : BM89 合并区间.py
# @Date    : 2022/06/28:23:47
"""
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。
输入：
[[10,30],[20,60],[80,100],[150,180]]

返回值：
[[10,60],[80,100],[150,180]]
"""
from typing import List


class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

    def __str__(self):
        return str(self.start) + "_" + str(self.end)

    def __repr__(self):
        return str(self.start) + "_" + str(self.end)

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
    print(Solution().merge([Interval(2, 3), Interval(1, 4)]))
