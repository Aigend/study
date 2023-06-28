# @File    : BM3 链表中的节点每k个一组翻转.py
# @Date    : 2022/07/07:22:28

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        # 先定义哨兵节点，求出链表的总长度
        dummy = ListNode(0)
        dummy.next = head
        lend = dummy.next
        i = 0
        while lend:
            i += 1
            lend = lend.next
        pre = dummy
        while i >= k:
            # 这一轮进行翻转
            for j in range(k-1):
                temp = head.next
                head.next = temp.next
                temp.next = pre.next
                pre.next = temp
            i = i - k
            pre = head
            head = head.next
        return dummy.next