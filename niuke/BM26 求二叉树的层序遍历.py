# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM26 求二叉树的层序遍历.py
# @Date    : 2022/07/13:23:32
# @Author  : jinwenlong@oppo.com
"""
描述
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树层序遍历的结果是
[
[3],
[9,20],
[15,7]

]


数据范围：二叉树的节点数满足 1 \le n \le 10^5 \1≤n≤10
5

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
# @return int整型二维数组
#

from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # write code here
        result = []
        if not root:
            return result
        q = deque()
        q.appendleft(root)
        while len(q):
            temp = []
            for i in range(len(q)): #这里不能用while循环
                t = q.pop()
                temp.append(t.val)
                if t.left:
                    q.appendleft(t.left)
                if t.right:
                    q.appendleft(t.right)
            result.append(temp)
        return result

if __name__ == '__main__':
    a=TreeNode(1)
    b=TreeNode(2)
    a.left = b
    print(Solution().levelOrder(a))