"""给定一个二叉树的中序与后序遍历结果，请你根据两个序列构造符合这两个序列的二叉树。
数据范围：二叉树的节点数满足 1≤n≤1000  ，节点上的值满足  ，保证节点的值各不相同
例如输入[2,1,4,3,5],[2,4,5,3,1]时，
根据中序遍历的结果[2,1,4,3,5]和后序遍历的结果[2,4,5,3,1]可构造出二叉树{1,2,3,#,#,4,5}，如下图所示："""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param inorder int整型一维数组 中序遍历序列
# @param postorder int整型一维数组 后序遍历序列
# @return TreeNode类
#
class Solution:
    result = []
    def buildTree(self , inorder: List[int], postorder: List[int]) -> TreeNode:
        # write code here
        # 自己写的case，有点问题，没打印#符号，但实际本题是要构造二叉树，
        # 下面的case未按题目要求作答
        # if postorder:
        #     Solution.result.append(postorder[-1])
        #     ind = inorder.index(postorder[-1])
        #     self.buildTree(inorder[:ind], postorder[:ind])
        #     self.buildTree(inorder[ind+1:], postorder[ind:-1])
        # return Solution.result

        # 网上的标准答案
        # if not inorder or not postorder:
        #     return None
        # root = TreeNode(postorder[-1])
        # idx = inorder.index(postorder[-1])
        # root.left = self.buildTree(inorder[:idx], postorder[:idx])
        # root.right = self.buildTree(inorder[idx + 1:], postorder[idx: -1])
        # return root

        if postorder:
            root = TreeNode(postorder[-1])
            idx = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:idx], postorder[:idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder[idx: -1])
            return root
        return None
