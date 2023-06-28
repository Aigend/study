# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM7 链表中环的入口结点.py
# @Date    : 2022/07/07:23:13
# @Author  : jinwenlong@oppo.com
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None #题上显示的是返回“null"，实际要返回None才能通过，题目中没有说清楚
        slow = pHead
        fast = pHead
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = pHead
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None