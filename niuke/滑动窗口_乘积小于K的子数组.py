"""
给定一个正整数数组 nums和整数 k 。
请找出该数组内乘积小于 k 的连续的子数组的个数。

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

输入: nums = [1,2,3], k = 0
输出: 0
"""

# 双指针
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        right = 0
        window_sum = 1
        result = 0

        while right < len(nums):
            window_sum *= nums[right]
            # 区间左侧边界向右
            while window_sum >= k:
                window_sum /= nums[left]
                left += 1

            # 区间右侧边界向右
            result += (right-left+1)   
            right += 1
        return result