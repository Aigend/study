# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM25 二叉树的后序遍历.py
# @Date    : 2022/07/13:23:25
# @Author  : jinwenlong@oppo.com
"""
描述
给定一个二叉树，返回他的后序遍历的序列。

后序遍历是值按照 左节点->右节点->根节点 的顺序的遍历。

数据范围：二叉树的节点数量满足 0 \le n \le 100 \0≤n≤100  ，二叉树节点的值满足 1 \le val \le 100 \1≤val≤100  ，树的各节点的值各不相同
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


class Solution:
    def postorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        result = []
        if not root:
            return result
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result
