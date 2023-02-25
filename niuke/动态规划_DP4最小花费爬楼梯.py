"""
描述
给定一个整数数组 cost \cost  ，其中 cost[i]\cost[i]  是从楼梯第i \i 个台阶向上爬需要支付的费用，下标从0开始。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

数据范围：数组长度满足 1 \le n \le 10^5 \1≤n≤10 
5
   ，数组中的值满足 1 \le cost_i \le 10^4 \1≤cost 
i
​
 ≤10 
4
  
输入描述：
第一行输入一个正整数 n ，表示数组 cost 的长度。
第二行输入 n 个正整数，表示数组 cost 的值。
输出描述：
输出最低花费

输入：
3
2 5 20
复制
输出：
5
复制
说明：
你将从下标为1的台阶开始，支付5 ，向上爬两个台阶，到达楼梯顶部。总花费为5 
"""
import sys

n = int(sys.stdin.readline().strip())
nums = sys.stdin.readline().split()
nums = [int(num) for num in nums]
dp =  [0 for i in range(n+1)]
for i in range(2, n+1):
    dp[i] = min(dp[i-1]+nums[i-1], dp[i-2]+nums[i-2])
sys.stdout.write(str(dp[n]))
