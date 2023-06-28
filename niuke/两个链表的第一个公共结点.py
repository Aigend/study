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
        # write code here
        head1 = pHead1
        head2 = pHead2

        # 这道题应该用while 循环，因为并不知道长度
        while pHead1 != pHead2:
            # 这里应该写遍历后，如果未找到相交点如何结束循环，避免while卡住

            # 仔细想了下，这里不用写结束条件，因为，最后肯定2个的值肯定是None
            # 如果提前结束循环，说明有交点，不然最后的值为None

            # 推荐写 pHead1 = head2 if not pHead1 else pHead1.next
            if pHead1 == None:
                pHead1 = head2
            else:
                pHead1 = pHead1.next

            if pHead2 == None:
                pHead2 = head1
            else:
                pHead2 = pHead2.next
        return pHead1

if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead1.next = ListNode(2)
    pHead1.next.next = ListNode(3)
    pHead1.next.next.next = ListNode(4)
    pHead2 = ListNode(5)
    pHead2.next = ListNode(6)
    pHead2.next.next = ListNode(7)
    print(Solution().FindFirstCommonNode(pHead1, pHead2))