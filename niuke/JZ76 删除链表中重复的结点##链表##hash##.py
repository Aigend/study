描述
在一个排序的链表中，存在重复的结点，
请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表 1->2->3->3->4->4->5  处理后为 1->2->5

class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        #空链表
        if pHead == None: 
            return None
        res = ListNode(0)
        #在链表前加一个表头
        res.next = pHead 
        cur = res
        while cur.next and cur.next.next: 
            #遇到相邻两个节点值相同
            if cur.next.val == cur.next.next.val: 
                temp = cur.next.val
                #将所有相同的都跳过
                while cur.next != None and cur.next.val == temp: 
                    cur.next = cur.next.next
            else:
                cur = cur.next
        #返回时去掉表头
        return res.next


class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        #空链表
        if pHead == None: 
            return None
        mp = dict()
        cur = pHead
        #遍历链表统计每个节点值出现的次数
        while cur: 
            if cur.val in mp:
                mp[cur.val] += 1
            else:
                mp[cur.val] = 1
            cur = cur.next
        res = ListNode(0)
        #在链表前加一个表头
        res.next = pHead 
        cur = res
        #再次遍历链表
        while cur.next: 
            #如果节点值计数不为1
            if mp[cur.next.val] != 1: 
                #删去该节点
                cur.next = cur.next.next 
            else:
                cur = cur.next
        #去掉表头
        return res.next 
