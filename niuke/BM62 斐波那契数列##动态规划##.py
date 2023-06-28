描述
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:

    def Fibonacci(self , n: int) -> int:
        # write code here
        if n < 3:
            return 1
        m = {1:1, 2:1}
        def dfs(m, n):
            if n > 2:
                if n not in m:
                    m[n] = dfs(m, n-1) + dfs(m, n-2)
                return m[n]
            return m[n]
        dfs(m, n)
        return m[n]
