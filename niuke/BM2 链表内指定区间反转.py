# @File    : BM2 链表内指定区间反转.py
# @Date    : 2022/07/07:21:47
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
