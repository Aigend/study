# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM15 删除有序链表中重复的元素-I.py
# @Date    : 2022/07/09:23:13
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
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        map = set() # 这里有个问题，题目要求空间复杂的为O(1), 这里为O(N),可以考虑改为使用字典的方式
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val not in map:
                map.add(head.val)
                pre.next = head
                pre = head
                head = head.next
            else:
                pre.next = head.next  # 这行代码必须要加，非则对最后一个重复的元素未处理
                head = head.next
        return dummy.next
