# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ6 从尾到头打印链表.py
# @Date    : 2022/08/08:20:18
# @Author  : jinwenlong@oppo.com

# 使用栈的方式
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param listNode ListNode类
# @return int整型一维数组
#
from typing import List
class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        # stack = []
        # while listNode:
        #     stack.append(listNode.val)
        #     listNode = listNode.next
        # return stack[::-1]

        # 递归
        import sys
        sys.setrecursionlimit(100000)
        if listNode:
            return self.printListFromTailToHead(listNode.next) + [listNode.val]
        return []

