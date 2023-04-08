
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
# 不考虑时间复杂度，简单算法
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # global i
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         nums.insert(i, target)
        #         return i
        # return i+1

        # 二分法
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left < len(nums):
            nums.insert(left, target)
        else:
            nums.append(target)
        print(nums)
        return left


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 2))
