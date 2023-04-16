"""
描述
给你一根长度为 n 的绳子，请把绳子剪成整数长的 m 段（ m 、 n 都是整数， n > 1 并且 m > 1 ， m <= n ），每段绳子的长度记为 k[1],...,k[m] 。
请问 k[1]*k[2]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18 。
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def cutRope(self , number: int) -> int:
        # write code here
        # //不超过3直接计算
        # if(target <= 3)
        #     return target- 1;
        # //dp[i]表示长度为i的绳子可以被剪出来的最大乘积
        
        dp = [0 for _ in range(number+1)]

        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5, number+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*dp[i-j])
        return dp[number]
