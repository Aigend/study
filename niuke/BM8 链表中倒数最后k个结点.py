# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM8 链表中倒数最后k个结点.py
# @Date    : 2022/07/07:23:46
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:

    def FindKthToTail(self, pHead: ListNode, k: int):
        # write code here
        # 这道题考虑用双指针，只遍历一遍就达到目的
        while not pHead or not k:
            return None
        dummy = ListNode(0)
        dummy.next = pHead
        left = dummy
        right = dummy
        for i in range(k):
            right = right.next
            if not right:
                return None
        while right.next:
            right = right.next
            left = left.next
        # return left
        return left.next
