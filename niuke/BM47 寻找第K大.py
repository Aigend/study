# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM47 寻找第K大.py
# @Date    : 2022/09/06:22:54
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
"""
    描述
    有一个整数数组，请你根据快速排序的思路，找出数组中第 k 大的数。

    给定一个整数数组 a ,同时给定它的大小n和要找的 k ，请返回第 k 大的数(包括重复的元素，不用去重)，保证答案存在。
    要求：时间复杂度 O(nlogn)O(nlogn)，空间复杂度 O(1)O(1)
    数据范围：0\le n \le 10^50≤n≤10
    5
     ， 1 \le K \le n1≤K≤n，数组中每个元素满足 0 \le val \le 10^90≤val≤10
    9

"""
import heapq
class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        # write code here
        if n >= K != 0:
            pq = []
            for i in range(K):
                # 构建一个k个大小的堆
                heapq.heappush(pq, a[i])
            for i in range(K, n):
                if pq[0] < a[i]:
                    heapq.heapreplace(pq, a[i])
            return heapq.heappop(pq)
        return 0
