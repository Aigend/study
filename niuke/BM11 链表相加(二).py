# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM11 链表相加(二).py
# @Date    : 2022/07/09:12:15
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:

    def revertList(self, pHead):
        """
        对传入的单个链表进行反转
        :param pHead:
        :return:
        """
        pre = None
        while pHead:
            temp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = temp
        return pre

    def addInList(self, head1: ListNode, head2: ListNode):
        # write code here
        # 思路：先反转链表，进行大数加法，对生成的结果再进行反转
        if not head1 or not head2:
            return None
        head1 = self.revertList(head1)
        head2 = self.revertList(head2)
        print("####")
        print(head1.val)
        print(head2.val)
        print("***")
        carry = 0
        dummy = ListNode(0)
        pre = dummy
        while head1 or head2:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            node = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            pre.next = node
            pre = node
            # 这里迭代的条件忘记写了，导致超时失败
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        if carry:
            node = ListNode(carry)
            pre.next = node
        return self.revertList(dummy.next)


if __name__ == '__main__':
    a = ListNode(9)
    b = ListNode(7)
    c = ListNode(3)
    a.next = b
    b.next = c
    e = ListNode(6)
    f = ListNode(3)
    e.next = f
    result = Solution().addInList(a, e)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)
    print(result.next.next.next.val)
