BM99_顺时针旋转矩阵

题目主要信息:
给定一个n∗n的矩阵，返回其顺时针90度旋转后的结果
举一反三：
学习完本题的思路你可以解决如下题目：

BM97. 旋转数组

方法：倒置翻转（推荐使用）
知识点：矩阵转置

矩阵转置是将上三角矩阵元素与下三角矩阵元素依据对角线位置对称互换，且该过程是可逆的。
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        #矩阵转置
        for i in range(n):
            for j in range(i):
                #交换上三角与下三角对应的元素
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
        #每行翻转
        for i in range(n):
            mat[i].reverse()
        return mat
