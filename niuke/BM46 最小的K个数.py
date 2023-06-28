# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM46 最小的K个数.py
# @Date    : 2022/07/25:23:08
# @Author  : jinwenlong@oppo.com
from typing import List


# class Solution:
#     def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
#         # write code here
#         res = []
#         if len(input) >= k and k != 0:
#             import heapq
#             #小根堆，每次输入要乘-1
#             pq = []
#             for i in range(k):
#                 #构建一个k个大小的堆
#                 heapq.heappush(pq, input[i])
#             print(pq)
#             for i in range(k, len(input)):
#                 #较小元素入堆
#                 print(input[i])
#                 if pq[0] > input[i]:
#                     print("##")
#                     heapq.heapreplace(pq, input[i])
#                 print("***")
#                 print(pq)
#             print(pq)
#             #堆中元素取出入数组
#             for i in range(k):
#                 res.append(pq[0])
#                 heapq.heappop(pq)
#         return res


class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        res = []
        if len(input) >= k != 0:
            import heapq
            # 小根堆，每次输入要乘-1
            pq = []
            for i in range(k):
                # 构建一个k个大小的堆
                heapq.heappush(pq, (-1 * input[i]))
            for i in range(k, len(input)):
                # 较小元素入堆
                if (-1 * pq[0]) > input[i]:
                    heapq.heapreplace(pq, (-1 * input[i]))
            # 堆中元素取出入数组
            for i in range(k):
                res.append(-1 * pq[0])
                heapq.heappop(pq)
        return res


if __name__ == '__main__':
    print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
