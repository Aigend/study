70_爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[n]
