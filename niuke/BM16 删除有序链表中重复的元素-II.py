# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM16 删除有序链表中重复的元素-II.py
# @Date    : 2022/07/09:23:26
# @Author  : jinwenlong@oppo.com

方法一：直接比较删除（推荐使用）
这是一个升序链表，重复的节点都连在一起，我们就可以很轻易地比较到重复的节点，然后将所有的连续相同的节点都跳过，连接不相同的第一个节点。
import java.util.*;
public class Solution {
    public ListNode deleteDuplicates (ListNode head) {
        //空链表
        if(head == null) 
            return null;
        ListNode res = new ListNode(0);
        //在链表前加一个表头
        res.next = head; 
        ListNode cur = res;
        while(cur.next != null && cur.next.next != null){ 
            //遇到相邻两个节点值相同
            if(cur.next.val == cur.next.next.val){ 
                int temp = cur.next.val;
                //将所有相同的都跳过
                while (cur.next != null && cur.next.val == temp) 
                    cur.next = cur.next.next;
            }
            else 
                cur = cur.next;
        }
        //返回时去掉表头
        return res.next; 
    }
}

方法二：哈希表（扩展思路）
知识点：哈希表
哈希表是一种根据关键码（key）直接访问值（value）的一种数据结构。而这种直接访问意味着只要知道key就能在O(1)时间内得到value，因此哈希表常用来统计频率、快速检验某个元素是否出现过等。
思路：
这道题幸运的是链表有序，我们可以直接与旁边的元素比较，然后删除重复。那我们扩展一点，万一遇到的链表无序呢？我们这里给出一种通用的解法，有序无序都可以使用，即利用哈希表来统计是否重复。
import java.util.*;
public class Solution {
    public ListNode deleteDuplicates (ListNode head) {
        //空链表
        if(head == null) 
            return null;
        Map<Integer,Integer> mp = new HashMap<>();
        ListNode cur = head;
        //遍历链表统计每个节点值出现的次数
        while(cur != null){ 
            if(mp.containsKey(cur.val))
                mp.put(cur.val, (int)mp.get(cur.val) + 1);
            else
                mp.put(cur.val,1);
            cur = cur.next;
        }
        ListNode res = new ListNode(0);
        //在链表前加一个表头
        res.next = head; 
        cur = res;
        //再次遍历链表
        while(cur.next != null){
            //如果节点值计数不为1 
            if(mp.get(cur.next.val) != 1) 
                //删去该节点
                cur.next = cur.next.next; 
            else
                cur = cur.next; 
        }
        //去掉表头
        return res.next; 
    }
}


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
import logging
import sys
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        dummy = ListNode(sys.maxsize)
        pre = dummy
        left = ListNode(0)
        while head and head.next:
            if head.val != left.val and head.val != head.next.val:
                pre.next = head
                pre = head
                left = head
                head = head.next
                pre.next = None #这里必须要加
            else:
                left = head
                head = head.next
        if head.val != left.val:
            pre.next = head
            pre.next.next =None
        return dummy.next


if __name__ == '__main__':
    a= ListNode(1)
    b= ListNode(2)
    c= ListNode(2)
    a.next = b
    b.next = c
    r= Solution().deleteDuplicates(a)
    # logging.warning(">>>>>>>>>>>>>>>>")
    while r:
        logging.warning(r.val)
        r = r.next
