"""
描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶(n为正整数)总共有多少种跳法。

数据范围：1 \le n \le 201≤n≤20
进阶：空间复杂度 O(1)O(1) ， 时间复杂度 O(1)O(1)
输入描述：
本题输入仅一行，即一个整数 n 
输出描述：


"""

import sys

for line in sys.stdin:
    a = line.split()

n = int(a[0])
dp = [0 for i in range(n+2)]
dp[1]=1
dp[2]=2
if n > 2:
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i] += dp[i-j]
        dp[i]+=1 
sys.stdout.write(str(dp[n]))