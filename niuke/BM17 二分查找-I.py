# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM17 二分查找-I.py
# @Date    : 2022/07/10:9:17
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
                if not nums:
                    return -1
                left = 0
                right = len(nums) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if nums[mid]  == target:
                        return mid
                    elif nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                if nums[left] == target:
                    return left
                return -1
        """
        left = 0
        right = len(nums) - 1
        while left <= right: # 这里建议写成<=的条件
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return -1




if __name__ == '__main__':
    print(Solution().search(
        [-1, 0, 3, 4, 6, 10, 13, 14], 13))
