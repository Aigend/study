题目主要信息：
将一棵n个节点的二叉树按照从上到下按层的方式打印，每层按照从左到右的顺序输出。

class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        res = []
        if pRoot is None:
            #如果是空，则直接返回空数组
            return res
        #队列存储，进行层次遍历
        q = [pRoot]
        while q:
            #记录二叉树的某一行
            row = []  
            n = len(q)
            #因先进入的是根节点，故每层节点多少，队列大小就是多少
            for i in range(n):
                #取出队首
                node = q.pop(0)
                row.append(node.val)
                #若是左右孩子存在，则存入左右孩子作为下一个层次
                if node.left:
                    #加入队尾
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row)
        return res
