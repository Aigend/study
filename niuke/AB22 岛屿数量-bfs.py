"""
给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组 
# @return int整型
#
from queue import Queue
class Solution:
    def solve(self , grid: List[List[str]]) -> int:
        # write code here
        #广度优先算法
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        q = Queue()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    grid[i][j]=0
                    result += 1
                    print(result)
                    q.put((i, j))
                    while not q.empty():
                        x, y = q.get()
                        if x-1>=0 and x-1<m and y>=0 and y<n and grid[x-1][y]=="1":
                            grid[x-1][y]=0
                            q.put((x-1, y))
                        if x+1>=0 and x+1<m and y>=0 and y<n and grid[x+1][y]=="1":
                            grid[x+1][y]=0
                            q.put((x+1, y))
                        if x>=0 and x<m and y-1>=0 and y-1<n and grid[x][y-1]=="1":
                            grid[x][y-1]=0
                            q.put((x, y-1))
                        if x>=0 and x<m and y+1>=0 and y+1<n and grid[x][y+1]=="1":
                            grid[x][y+1]=0
                            q.put((x, y+1))
        return result  
