# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM10 两个链表的第一个公共结点.py
# @Date    : 2022/07/08:23:46
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 复杂了
        # if not pHead1 or not pHead2:
        #     return None
        # a = pHead1
        # b = pHead2
        # a_flag = True
        # b_flag = True
        # while pHead1 is not pHead2:
        #     pHead1 = pHead1.next
        #     pHead2 = pHead2.next
        #     # if pHead1 is pHead2 and not pHead1:
        #     if pHead1 is pHead2:
        #         return pHead1
        #     if not pHead1 and a_flag:
        #         pHead1 = b
        #         a_flag = False
        #     if not pHead2 and b_flag:
        #         pHead2 = a
        #         b_flag = False
        # return pHead1

        # 方法二 逻辑清晰
        if not pHead1 or not pHead2:
            return None
        head1 = pHead1
        head2 = pHead2
        while pHead1 is not pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
            if pHead1 is pHead2:
                return pHead1
            pHead1 = head2 if pHead1 is None else pHead1
            pHead2 = head1 if pHead2 is None else pHead2
        return pHead1