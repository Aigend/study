# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM29 二叉树中和为某一值的路径(一).py
# @Date    : 2022/07/17:21:40
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
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 空节点找不到路径
        if not root:
            return False
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
