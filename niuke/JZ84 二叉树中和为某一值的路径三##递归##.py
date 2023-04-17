描述
给定一个二叉树root和一个整数值 sum ，求该树有多少路径的的节点值之和等于 sum 。
1.该题路径定义不需要从根节点开始，也不需要在叶子节点结束，但是一定是从父亲节点往下到孩子节点
2.总节点数目为n
3.保证最后返回的路径个数在整形范围内(即路径个数小于231-1)

class Solution:
    def __init__(self):
        self.res = 0
        
    #dfs查询以某节点为根的路径数
    def dfs(self, root: TreeNode, sum: int):
        if root is None:
            return
        #符合目标值
        if sum == root.val: 
            self.res += 1
        #进入子节点继续找
        self.dfs(root.left, sum - root.val) 
        self.dfs(root.right, sum - root.val)
    
    def FindPath(self , root: TreeNode, sum: int) -> int:
        #为空则返回
        if root is None:
            return self.res
        #查询以某节点为根的路径数
        self.dfs(root, sum) 
        #以其子节点为新根
        self.FindPath(root.left, sum); 
        self.FindPath(root.right, sum)
        return self.res
