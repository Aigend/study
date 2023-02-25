"""
输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。

"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                count = 1
            result = max(result, count)
        return result

"""
# 双指针
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        right = 0
        length = len(nums)
        result = 0
        for i in range(length):
            if nums[i] > nums[right]:
                right += 1
            else:
                left = i
                right = i
            result = max(result, right-left+1)
        return result
"""