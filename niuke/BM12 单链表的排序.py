# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM12 单链表的排序.py
# @Date    : 2022/07/09:21:38
# @Author  : jinwenlong@oppo.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self, head: ListNode):
        # 方法1，链表的排序转成数组进行排序，完成后，修改链表的值
        # pHead = head
        # nums = []
        # while pHead:
        #     nums.append(pHead.val)
        #     pHead = pHead.next
        # nums.sort()
        # pHead = head
        # for num in nums:
        #     pHead.val = num
        #     pHead = pHead.next
        # return head

        # write code here 分治法
        # 首先链表只有一个节点或没有节点的情况
        if not head or not head.next:
            return head
        # 创建快慢两种指针
        slow, fast = head, head
        # 去找中间位置来切断链表
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None  # 找到左右两部分
        left, right = self.sortInList(head), self.sortInList(mid)  # 一直递归下去，直到左右两部分的节点都被切割开
        # 分别对左右两边进行排序（升序）并合并
        res = ListNode(0)
        tail = res
        while left and right:
            if left.val < right.val:  # 如果左边节点的值时小于右边的时候
                tail.next, left = left, left.next  # 那么tail将会在左边进行排序；否则在右边
            else:
                tail.next, right = right, right.next
            tail = tail.next
        # 仅有左边或右边的情况
        if left:
            tail.next = left
        if right:
            tail.next = right
        return res.next
