
"""
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

这里的子数组是连续的
"""


# 双指针
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window_sum = 0
        result = len(nums) + 1

        while right < len(nums):
            window_sum += nums[right]
            while window_sum >= target:
                result = min(result, right-left+1)
                window_sum -= nums[left]
                left += 1

            right += 1
        if result != len(nums) + 1:
            return result
        else:
            return 0