# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : BM61 矩阵最长递增路径.py
# @Date    : 2022/09/06:20:41
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
"""
    描述
    给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。
    你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。并输出这条最长路径的长度。
    这个路径必须满足以下条件：

    1. 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
    2. 你不能走重复的单元格。即每个格子最多只能走一次。

    数据范围：1 \le n,m \le 10001≤n,m≤1000，0 \le matrix[i][j] \le 10000≤matrix[i][j]≤1000
    进阶：空间复杂度 O(nm)O(nm) ，时间复杂度 O(nm)O(nm)

    例如：当输入为[[1,2,3],[4,5,6],[7,8,9]]时，对应的输出为5，
    其中的一条最长递增路径如下图所示：
"""
class Solution:
    def solve(self , matrix: List[List[int]]) -> int:
        # write code here
        if not matrix or not matrix[0]:
            return 0
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(matrix, x, y, dp):
            if dp[x][y] != 0:
                return dp[x][y]
            x_partion = [-1, 1, 0, 0]
            y_partion = [0, 0, -1, 1]
            for i in range(len(x_partion)):
                x_new = x + x_partion[i]
                y_new = y + y_partion[i]
                if x_new >= 0 and x_new < m and y_new >=0 and y_new < n and matrix[x_new][y_new] > matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(matrix, x_new, y_new, dp)+1)
            return dp[x][y]
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(matrix, i, j, dp))
        return result + 1