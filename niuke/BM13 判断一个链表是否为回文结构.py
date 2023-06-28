# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM13 判断一个链表是否为回文结构.py
# @Date    : 2022/07/09:22:13
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPail(self, head: ListNode) -> bool:
    # write code here
    s = []
    while head:
        s.append(head.val)
        head = head.next
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

"""
class Solution:
    #反转链表指针
    def reverse(self, head:ListNode): 
        #前序节点
        prev = None 
        while head:
            #断开后序
            next = head.next 
            #指向前序
            head.next = prev 
            prev = head
            head = next
        return prev
    
    def isPail(self , head: ListNode) -> bool:
        p = head
        n = 0
        #找到链表长度
        while p : 
            n += 1
            p = p.next
        #中点
        n = (int)(n / 2) 
        p = head
        while n > 0:
            p = p.next
            n -= 1
        #中点处反转
        p = self.reverse(p) 
        q = head
        while p:
            #比较判断节点值是否相等
            if p.val != q.val: 
                return False
            p = p.next
            q = q.next
        return True

"""