"""
描述
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。

数据范围: 1 \le n,m\le 5001≤n,m≤500，矩阵中任意值都满足 0 \le a_{i,j} \le 1000≤a 
i,j
​
 ≤100
要求：时间复杂度 O(nm)O(nm)

例如：当输入[[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]时，对应的返回值为12，
所选择的最小累加和路径如下图所示：
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # write code here
        m = len(matrix)
        n = len(matrix[0])

        # 二维的数组实际上指向的是同一个引用，这是因为python中 [list] * number 事实上是一个浅复制，
        # 所以第二维的数组事实上没有内存独立
        # dp = [[0]*n]*m
        dp = [[0 for _ in range(n)] for _ in range(m)]

        
        dp[0][0]=matrix[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for j in range(1, n):
            dp[0][j]=dp[0][j-1]+matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+matrix[i][j]
        return dp[i-1][j-1]

if __name__ == "__main__":
    print(Solution().minPathSum)