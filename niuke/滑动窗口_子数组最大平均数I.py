"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k:int) -> int:
        result = 0
        tempSum = sum(nums[:k])
        result = max(result, tempSum)
        for j in range(k, len(nums)):
            tempSum = tempSum  + nums[j] - nums[j-k]
            result = max(result, tempSum)
        return result/k