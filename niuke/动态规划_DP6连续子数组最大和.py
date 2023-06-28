"""
描述
给定一个长度为 n\n 的数组，数组中的数为整数。
请你选择一个非空连续子数组，使该子数组所有数之和尽可能大，子数组最小长度为1。求这个最大值。
输入描述：
第一行为一个正整数 n\n ，代表数组的长度。 1\leq n \leq2*10^51≤n≤2∗10 
5
 
第二行为 n\n 个整数 a_ia 
i
​
 ，用空格隔开，代表数组中的每一个数。 |a_i| \leq 10^2∣a 
i
​
 ∣≤10 
2
 
输出描述：
连续子数组的最大之和。
示例1
输入：
8
1 -2 3 10 -4 7 2 -5
复制
输出：
18
复制
说明：
经分析可知，输入数组的子数组[3,10,-4,7,2]可以求得最大和为18    
"""

import sys

n = int(sys.stdin.readline().strip())
nums = [int(num) for num in sys.stdin.readline().split()]

dp = [0 for _ in range(n)]
dp[0]=nums[0]

result = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])
    if dp[i]>result:
        result = dp[i]
sys.stdout.write(str(result))
