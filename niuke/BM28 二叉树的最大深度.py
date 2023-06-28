# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM28 二叉树的最大深度.py
# @Date    : 2022/07/17:21:38
# @Author  : jinwenlong@oppo.com
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
# @return int整型
#
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # write code here
        if not root:
            return 0
        #         left = self.maxDepth(root.left)
        #         right = self.maxDepth(root.right)
        #         return max(left, right)+1

        import queue
        q = queue.Queue()
        q.put(root)
        result = 0
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                top = q.get()
                if top.left:
                    q.put(top.left)
                if top.right:
                    q.put(top.right)
            result += 1
        return result







