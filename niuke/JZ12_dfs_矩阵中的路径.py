"""
描述
请设计一个函数，用来判断在一个n乘m的矩阵中是否存在一条包含某长度为len的字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
​
  矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
数据范围：0 \le n,m \le 20\0≤n,m≤20 ,1\le len \le 25\1≤len≤25 
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix char字符型二维数组 
# @param word string字符串 
# @return bool布尔型
#
class Solution:
    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        # write code here
        if len(matrix) == 0:
          return False
        n = len(matrix)
        m = len(matrix[0])
        #初始化flag矩阵记录是否走过
        flag = [[False for i in range (m)] for j in range(n)]
        #遍历矩阵找起点
        for i in range(n):
          for j in range(m):
            #通过dfs找到路径
            if self.dfs(matrix, n, m, i, j, word, 0, flag):
              return True
        return False

    def dfs(self, matrix: List[List[str]], n: int, m: int, i: int, j: int, word: str, k: int, flag: List[List[bool]]) -> bool:
          if i < 0 or i >= n or j < 0 or j >= m or (matrix[i][j] != word[k]) or flag[i][j]:
              #下标越界、字符不匹配、已经遍历过不能重复
              return False
          #k为记录当前第几个字符
          if k == len(word) - 1:
              return True
          flag[i][j] = True
          #该结点任意方向可行就可
          if (self.dfs(matrix, n, m, i - 1, j, word, k + 1, flag)
              or self.dfs(matrix, n, m, i + 1, j, word, k + 1, flag)
              or self.dfs(matrix, n, m, i, j - 1, word, k + 1, flag)
              or self.dfs(matrix, n, m, i , j + 1, word, k + 1, flag)):
              return True
          #没找到经过此格的，此格未被占用
          flag[i][j] = False
          return False