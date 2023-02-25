# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM4 合并两个排序的链表.py
# @Date    : 2022/07/07:22:46
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
"""
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        cur1 = pHead1
        cur2 = pHead2
        if not cur1:
            return cur2
        if not cur2:
            return cur1

        # 1.确定新链表头结点
        result = ListNode(-1)
        new_cur = result
        # 2.依次比较其他节点
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                new_cur.next = cur1
                cur1 = cur1.next
            else:
                new_cur.next = cur2
                cur2 = cur2.next
            new_cur = new_cur.next
        # 次循环结束后，cur1和cur2一定有一个为None
        new_cur.next = cur1 if cur1 else cur2
        return result.next
"""


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        dummy = ListNode(0)
        pre = dummy
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                pre.next = pHead2
                pHead2 = pHead2.next
            else:
                pre.next = pHead1
                pHead1 = pHead1.next
            pre = pre.next
        if pHead1:
            pre.next = pHead1
        elif pHead2:
            pre.next = pHead2
        return dummy.next

