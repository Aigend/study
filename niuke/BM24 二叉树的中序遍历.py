# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM24 二叉树的中序遍历.py
# @Date    : 2022/07/13:23:17
# @Author  : jinwenlong@oppo.com
"""
描述
给定一个二叉树的根节点root，返回它的中序遍历结果。

数据范围：树上节点数满足 0 \le n \le 10000≤n≤1000，树上每个节点的值满足 0 \le val \le 10000≤val≤1000
进阶：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#

from typing import List

import sys
sys.setrecursionlimit(1500)

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        result = []
        if not root:
            return result

        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result
