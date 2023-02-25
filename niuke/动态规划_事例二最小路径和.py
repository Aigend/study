"""
给定一个包含非负整数的 *m* x *n* 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

DP定义及状态方程
定义dp[i][j]表示到达（i,j）坐标处的最小路径和，达到(i,j)处只能通过两条路(i-1,j)与(i,j-1),选择其中路径和最小的一个即可，因此递推方程为dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + gird[i][j]

此题目的最终答案即为dp数组中的最后一个值：dp[-1][-1]

初始边界条件
初始化过程，对于第一列从上往下走，第一行只能从左往右走：
因此dp[i][0]=dp[i-1][0]+grid[i][0], dp[0][j]=dp[0][j-1]+grid[0][j]

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

        #求最小和的路径：
        result_path = []
        r = m - 1
        c = n - 1
        while True:
            if r-1 >= 0 and c-1 >= 0:
                if dp[r - 1][c] < dp[r][c - 1]:
                    # result_path.append(in_matrix[r - 1][c])
                    result_path.append(grid[r - 1][c])
                    r = r - 1
                else:
                    # result_path.append(in_matrix[r][c - 1])
                    result_path.append(grid[r][c - 1])
                    c = c - 1
            elif r == 0 and c-1 >= 0:
                while c-1 >= 0:
                    # result_path.append(in_matrix[0][c-1])
                    result_path.append(grid[0][c-1])
                    c = c - 1
            elif c == 0 and r-1 >= 0:
                while r-1 >= 0:
                    # result_path.append(in_matrix[r-1][0])
                    result_path.append(grid[r-1][0])
                    r = r - 1
            else:
                break

        return dp[-1][-1]
