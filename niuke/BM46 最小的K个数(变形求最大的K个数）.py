# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM46 最小的K个数(变形求最大的K个数）.py
# @Date    : 2022/07/25:23:50
# @Author  : jinwenlong@oppo.com
from typing import List


class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        res = []
        n = len(input)
        if n >= k != 0:
            import heapq
            pq = []
            for i in range(k):
                # 构建一个k个大小的堆
                heapq.heappush(pq, input[i])
            for i in range(k, n):
                if pq[0] < input[i]:
                    heapq.heapreplace(pq, input[i])
            # 堆中元素取出入数组
            for i in range(k):
                res.append(pq[0])
                heapq.heappop(pq)
        return res


if __name__ == '__main__':
    print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))