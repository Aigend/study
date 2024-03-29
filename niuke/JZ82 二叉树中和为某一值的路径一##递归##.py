描述
给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
2.叶子节点是指没有子节点的节点
3.路径只能从父节点到子节点，不能从子节点到父节点
4.总节点数目为n

class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # 空节点找不到路径
        if not root: 
            return False
        # 叶子节点，且路径和为sum
        if not root.left and not root.right and sum - root.val == 0:
            return True
        # 递归进入子节点
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
