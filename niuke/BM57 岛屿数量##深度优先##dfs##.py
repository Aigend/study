BM57 岛屿数量##深度优先##dfs##
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    def solve(self , grid: List[List[str]]) -> int:
        # write code here
        if not grid:
            return 0
        result = 0
        def dfs(grid, i, j):
            grid[i][j] = "0"
            m = len(grid)
            n = len(grid[0])
            for x, y in [(i-1, j),(i+1, j), (i,j-1), (i, j+1)]:
                if x>=0 and x<m and y >= 0 and y < n and grid[x][y]=="1":
                    dfs(grid, x, y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    dfs(grid, i, j)
        return result
