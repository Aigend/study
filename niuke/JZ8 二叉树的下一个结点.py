# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ8 二叉树的下一个结点.py
# @Date    : 2022/08/08:21:17
# @Author  : jinwenlong@oppo.com
class Solution:
    """
    输入分为2段，第一段是整体的二叉树，第二段是给定二叉树节点的值，
    后台会将这2个参数组装为一个二叉树局部的子树传入到函数GetNext里面，用户得到的输入只有一个子树根节点
    """
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right !=None:
            pNode = pNode.right
            while pNode.left !=None:
                pNode =pNode.left
            return pNode
        while pNode.next !=None:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None


class Solution1:
    nodes = []

    def GetNext(self, pNode):
        # 查找根节点
        root = pNode
        while root.next:
            root = root.next

        # 中序遍历打造nodes
        self.InOrder(root)

        # 匹配节点
        for i in range(len(self.nodes) - 1):
            cur = self.nodes[i]
            if pNode == cur:
                return self.nodes[i + 1]
        return None

    # 中序遍历
    def InOrder(self, root):
        if root == None:
            return
        self.InOrder(root.left)
        self.nodes.append(root)
        self.InOrder(root.right)


