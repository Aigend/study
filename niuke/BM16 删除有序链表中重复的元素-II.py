# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM16 删除有序链表中重复的元素-II.py
# @Date    : 2022/07/09:23:26
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
# @return ListNode类
#
import logging
import sys
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        dummy = ListNode(sys.maxsize)
        pre = dummy
        left = ListNode(0)
        while head and head.next:
            if head.val != left.val and head.val != head.next.val:
                pre.next = head
                pre = head
                left = head
                head = head.next
                pre.next = None #这里必须要加
            else:
                left = head
                head = head.next
        if head.val != left.val:
            pre.next = head
            pre.next.next =None
        return dummy.next


if __name__ == '__main__':
    a= ListNode(1)
    b= ListNode(2)
    c= ListNode(2)
    a.next = b
    b.next = c
    r= Solution().deleteDuplicates(a)
    # logging.warning(">>>>>>>>>>>>>>>>")
    while r:
        logging.warning(r.val)
        r = r.next