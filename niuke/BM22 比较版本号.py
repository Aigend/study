# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM22 比较版本号.py
# @Date    : 2022/08/31:22:38
# @Author  : jinwenlong@oppo.com
class Solution:
    def compare(self, version1: str, version2: str) -> int:
        # 分割
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        for i in range(max([len(nums1), len(nums2)])):
            # 较短的版本号后续都取0,字符串转数字
            num1 = int(nums1[i]) if i < len(nums1) else 0
            num2 = int(nums2[i]) if i < len(nums2) else 0
            # 比较数字大小
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        # 版本相同
        return 0
