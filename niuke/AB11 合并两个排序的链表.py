
"""

如输入{1,3,5},{2,4,6}时，合并后的链表为{1,2,3,4,5,6}，所以对应的输出为{1,2,3,4,5,6}，转换过程如下图所示：
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        dummy = ListNode(0)
        pre = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pre.next = pHead1
                pre=pHead1
                pHead1 = pHead1.next
            else:
                pre.next = pHead2
                pre=pHead2
                pHead2=pHead2.next
        if pHead1:
            pre.next=pHead1
        elif pHead2:
            pre.next=pHead2
        return dummy.next
            
