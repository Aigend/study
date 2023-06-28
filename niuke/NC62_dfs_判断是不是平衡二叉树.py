"""
描述
输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
样例解释：
"""
from enum import Flag


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return bool布尔型
#
class Solution:
    flag = True
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        self.maxDepth(pRoot)
        return Solution.flag
        
        
    def maxDepth(self, node:TreeNode)->int:
        if not node:
            return 0
        left = self.maxDepth(node.left)
        if left == -1:
            return -1
        right = self.maxDepth(node.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            Solution.flag = False
            return -1
        return max(left, right) + 1