描述
一个机器人在m×n大小的地图的左上角（起点）。
机器人每次可以向下或向右移动。机器人要到达地图的右下角（终点）。
可以有多少种不同的路径从起点走到终点？

import sys
#设置递归深度
sys.setrecursionlimit(100000) 
class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        #矩阵只要有一条边为1，路径数就只有一种了
        if m == 1 or n == 1: 
            return 1
        else: 
            #两个分支
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        #dp[i][j]表示大小为i*j的矩阵的路径数量
        dp = [[0] * (n + 1) for i in range(m + 1)] 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #只有1行的时候，只有一种路径
                if i == 1: 
                    dp[i][j] = 1
                    continue
                #只有1列的时候，只有一种路径
                if j == 1: 
                    dp[i][j] = 1
                    continue
                #路径数等于左方格子的路径数加上上方格子的路径数
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 
        return dp[m][n]
