"""
描述
请设计一个函数，用来判断在一个n乘m的矩阵中是否存在一条包含某长度为len的字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 ​
  矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。"""
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
        m = len(matrix)
        n = len(matrix[0])
        flag = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == word[0]:
                    if self.dfs(matrix, word, m, n, i, j, 0, flag):
                        return True
        return False
    
    def dfs(self, matrix, word, m, n, i, j, k, flag):
        if (i < 0 or i >= m) or (j<0 or j >= n) or matrix[i][j]!= word[k] or flag[i][j]== True:
            return False
        if k == len(word) - 1:
            return True
        flag[i][j]= True
        if self.dfs(matrix, word, m, n, i-1, j, k+1, flag) or \
            self.dfs(matrix, word, m, n, i+1, j, k+1, flag) or \
            self.dfs(matrix, word, m, n, i, j-1, k+1, flag) or \
            self.dfs(matrix, word, m, n, i, j+1, k+1, flag):
            return True
        flag[i][j]=False  # 这一步别忘记了
        return False
