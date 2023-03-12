"""
请你实现一个链表。
操作：
insert x y：将
�
y加入链表，插入在第一个值为
�
x的结点之前。若链表中不存在值为
�
x的结点，则插入在链表末尾。保证
�
x,
�
y为int型整数。
delete x：删除链表中第一个值为
�
x的结点。若不存在值为
�
x的结点，则不删除。
输入描述：
第一行输入一个整数
�
n (
1
≤
�
≤
1
0
4
1≤n≤10 
4
 )，表示操作次数。
接下来的
�
n行，每行一个字符串，表示一个操作。保证操作是题目描述中的一种。
输出描述：
输出一行，将链表中所有结点的值按顺序输出。若链表为空，输出"NULL"(不含引号)。
"""
import sys
stack = []
num = int(input())
for i in range(num):
    ipt = input().split()
    if ipt[0]=="insert":
        x, y = ipt[1], ipt[2]
        if x in stack:
            ind =  stack.index(x)
            stack.insert(ind, y)
        else:
            stack.append(y)
    elif ipt[0]=="delete":
        if ipt[1] in stack:
            stack.remove(ipt[1])
if not stack:
    print("NULL")
else:
    print(" ".join(stack))
