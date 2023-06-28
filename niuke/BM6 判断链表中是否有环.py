# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM6 判断链表中是否有环.py
# @Date    : 2022/07/07:22:53
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

