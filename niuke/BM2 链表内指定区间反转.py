# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM2 链表内指定区间反转.py
# @Date    : 2022/07/07:21:47
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        head = pre.next
        for j in range(n - m):
            temp = head.next
            head.next = temp.next
            # temp.next = head
            temp.next = pre.next
            pre.next = temp
        return dummy.next
