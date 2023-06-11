描述
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。

具体做法：

step 1：我们可以构造一个与矩阵同样大小的二维辅助数组，其中dp[i][j]表示以(i,j)位置为终点的最短路径和，则dp[0][0]=matrix[0][0]。
step 2：很容易知道第一行与第一列，只能分别向右或向下，没有第二种选择，因此第一行只能由其左边的累加，第一列只能由其上面的累加。
step 3：边缘状态构造好以后，遍历矩阵，补全矩阵中每个位置的dp数组值：如果当前的位置是
(i，j)，上一步要么是(i−1,j)往下，要么就是(i,j−1)往右，那么取其中较小值与当前位置的值相加就是到当前位置的最小路径和，因此状态转移公式为
dp[i][j]=min(dp[i−1][j],dp[i][j−1])+matrix[i][j]。
step 4：最后移动到(n−1,m−1)的位置就是到右下角的最短路径和。

class Solution:
    def minPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 因为n,m均大于等于1
        m = len(matrix[0])
        # dp[i][j]表示以当前i，j位置为终点的最短路径长度
        dp = [[0] * m for i in range(n)]
        dp[0][0] = matrix[0][0]
        # 处理第一列
        for i in range(1, n):
            dp[i][0] = matrix[i][0] + dp[i - 1][0]
        # 处理第一行
        for j in range(1, m):
            dp[0][j] = matrix[0][j] + dp[0][j - 1]
        # 其他按照公式来
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = matrix[i][j] + min(dp[i][j-1], dp[i-1][j])
                # if dp[i - 1][j] > dp[i][j - 1]:
                #     dp[i][j] = matrix[i][j] + dp[i][j - 1]
                # else:
                #     dp[i][j] = matrix[i][j] + dp[i - 1][j]
        return dp[n - 1][m - 1]
