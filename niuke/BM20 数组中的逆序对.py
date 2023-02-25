# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM20 数组中的逆序对.py
# @Date    : 2022/08/31:22:13
# @Author  : jinwenlong@oppo.com
# write code here

# def merge_count(left, right):
#     l = 0
#     r = 0
#     data_tmp = []
#     count = 0
#     while l < len(left) and r < len(right):
#         if right[r] < left[l]:
#             data_tmp.append(right[r])
#             count = count + len(left) - l
#             r = r + 1
#         else:
#             data_tmp.append(left[l])
#             l = l + 1
#     while l < len(left):
#         data_tmp.append(left[l])
#         l = l + 1
#     while r < len(right):
#         data_tmp.append(right[r])
#         r = r + 1
#     return data_tmp, count
#
#
# def merge(data):
#     n = len(data)
#     mid = n // 2
#     if n <= 1:
#         return data, 0
#     if n >= 2:
#         left, count_left = merge(data[0:mid])
#         right, count_right = merge(data[mid:])
#         orderlist, count_list = merge_count(left, right)
#         count = (count_left + count_right + count_list)
#     return orderlist, count
#
#
# orderlist, count = merge(data)
# return count % 1000000007


class Solution:
    mod = 1000000007

    def MergeSort(self, left: int, right: int, data: List[int], temp: List[int]) -> int:
        # 停止划分
        if left >= right:
            return 0
        # 取中间
        mid = int((left + right) / 2)
        # 左右划分合并
        res = self.MergeSort(left, mid, data, temp) + self.MergeSort(mid + 1, right, data, temp)
        # 防止溢出
        res %= self.mod
        i, j = left, mid + 1
        for k in range(left, right + 1):
            temp[k] = data[k]
        for k in range(left, right + 1):
            if i == mid + 1:
                data[k] = temp[j]
                j += 1
            elif j == right + 1 or temp[i] <= temp[j]:
                data[k] = temp[i]
                i += 1
            # 左边比右边大，答案增加
            else:
                data[k] = temp[j]
                j += 1
                # 统计逆序对
                res += mid - i + 1
        return res % self.mod

    def InversePairs(self, data: List[int]) -> int:
        n = len(data)
        res = [0 for i in range(n)]
        return self.MergeSort(0, n - 1, data, res)
