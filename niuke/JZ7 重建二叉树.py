# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ7 重建二叉树.py
# @Date    : 2022/08/08:20:28
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
# 输入：
# [1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
# 复制
# 返回值：
# {1,2,3,4,#,5,6,#,7,#,#,8}
# 复制
# 说明：
# 返回根节点，系统会输出整颗二叉树对比结果，重建结果如题面图示
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
from typing import List


class Solution:
    def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        # 递归
        index = {val: i for i, val in enumerate(vin)}

        def build(preRootId, inL, inR):
            if inL > inR:
                return None
            rootVal = pre[preRootId]
            inRootId = index[rootVal]
            leftSize = inRootId - inL
            root = TreeNode(rootVal)
            root.left = build(preRootId + 1, inL, inRootId - 1)
            root.right = build(preRootId + leftSize + 1, inRootId + 1, inR)
            return root

        return build(0, 0, len(pre) - 1)
