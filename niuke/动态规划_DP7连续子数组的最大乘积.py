"""
描述
输入一个长度为 n 的整型数组 nums，数组中的一个或连续多个整数组成一个子数组。求所有子数组的乘积的最大值。
1.子数组是连续的，且最小长度为 1 ，最大长度为 n
2.长度为 1 的子数组，乘积视为其本身，比如 [4] 的乘积为 4
3.该题的数据保证最大的乘积不会超过 int 的范围，即不超过2^{32}-12 
32
 −1
数据范围:
1 <= n <= 2\times10^51<=n<=2×10 
5
 
-100 <= a[i] <= 100−100<=a[i]<=100
输入描述：
第一行输入一个正整数 n ，表示数组的长度
第二行输入 n 个整数，表示数组中的值。
输出描述：
输出子数组的乘积的最大值
示例1
输入：
4
3 2 -2 4
复制
输出：
6
复制
说明：
子数组[3,2]的乘积为6，[3,2,-1,4]的乘积为-24，[4]的乘积为4，故返回6
"""

import sys

n = int(sys.stdin.readline().strip())
nums = [int(num) for num in sys.stdin.readline().split()]

dp = [0 for _ in range(n)]
dp[0]=nums[0]
maxnum = dp[0]
minnum = dp[0]
result = dp[0]

for num in nums[1:]:
    n1, n2 = num * maxnum, num * minnum
    maxnum = max(n1, n2, num)
    minnum = min(n1, n2, num)
    if maxnum>result:
        result = maxnum
sys.stdout.write(str(result))