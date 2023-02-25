# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM1 反转链表.py
# @Date    : 2022/07/04:23:35
# @Author  : jinwenlong@oppo.com
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def ReverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
