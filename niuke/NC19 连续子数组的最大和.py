"""
描述
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，子数组最小长度为1。求所有子数组的和的最大值。
数据范围:
1 <= n <= 2\times10^51<=n<=2×10 
5
 
-100 <= a[i] <= 100−100<=a[i]<=100

要求:时间复杂度为 O(n)O(n)，空间复杂度为 O(n)O(n)
进阶:时间复杂度为 O(n)O(n)，空间复杂度为 O(1)O(1)
示例1
输入：
[1,-2,3,10,-4,7,2,-5]
复制
返回值：
18
复制
说明：
经分析可知，输入数组的子数组[3,10,-4,7,2]可以求得最大和为18  
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        import sys

        n = len(array)
        nums = array

        dp = [0 for _ in range(n)]
        dp[0]=nums[0]

        result = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i]>result:
                result = dp[i]
        return result