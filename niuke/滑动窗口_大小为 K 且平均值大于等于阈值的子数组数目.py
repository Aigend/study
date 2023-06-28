"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

 输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

"""

# 滑动窗口
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        window_sum = 0
        result = 0

        while right < len(arr):
            # 更新窗口内数的求和
            window_sum += arr[right]
            if right - left + 1 == k:
                # 判断窗口内数的和与平均值的和
                if window_sum >= k*threshold:
                    result += 1
                # 窗口左边界向右移动
                window_sum -= arr[left]
                left += 1 
            # 窗口右边界向右移动
            right += 1
        return result