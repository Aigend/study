
# @File    : BM9 删除链表的倒数第n个节点.py
# @Date    : 2022/07/08:23:32

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) :
        # write code here
        if not head or not n:
            return None
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy
        for i in range(n):
            right = right.next
            if not right:
                return None
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
