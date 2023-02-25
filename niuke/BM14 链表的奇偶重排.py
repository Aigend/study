# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM14 链表的奇偶重排.py
# @Date    : 2022/07/09:22:23
# @Author  : jinwenlong@oppo.com
import time


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
# a = ListNode(0)
# b = ListNode(0)
# print(id(a))
# print(id(b))
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd = odd_dummy
        even = even_dummy
        i = 1
        while head:
            if i:
                odd.next = head
                odd = head
                i = 0
            else:
                even.next = head
                even = head
                i = 1
            head = head.next
        odd.next = even_dummy.next
        even.next = None #不设置会导致超时，因为偶数位的最后一位元素后面不是为None,会导致一个环
        return odd_dummy.next


if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(1)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    g = ListNode(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    h = Solution().oddEvenList(a)
    print("####")
    while h:
        print(h.val)
        h = h.next
    # print(h.val)
    # print(h.next.val)
    # print(h.next.next.val)
    # print(h.next.next.next.val)
    # print(h.next.next.next.next.val)
    # print(h.next.next.next.next.next.val)
    # print(h.next.next.next.next.next.next.val)
    # print(h.next.next.next.next.next.next.next.val)
    # print(h.next.next.next.next.next.next.next.next.val)
