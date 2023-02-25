# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM27 按之字形顺序打印二叉树.py
# @Date    : 2022/07/13:23:59
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
# @return int整型二维数组
#

from typing import List
import queue

class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        # write code here
        result = []
        if not pRoot:
            return result
        q = queue.Queue()
        q.put(pRoot)
        flag = True
        while not q.empty():
            temp = []
            size = q.qsize()
            flag = not flag
            for i in range(size): #这里不能用while循环
                t = q.get()
                temp.append(t.val)
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)
            if flag:
                temp = temp[::-1]
            result.append(temp)
        return result


if __name__ == '__main__':
    a=TreeNode(1)
    b=TreeNode(2)
    a.left = b
    print(Solution().Print(a))