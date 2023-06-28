"""
请你实现一个循环队列，该循环队列可利用的空间大小等于n个int型变量的大小。
操作：
push x：将x加入到循环队列尾端。若循环队列已满，输出"full"(不含引号)，否则不输出任何内容。保证x为int型整数。
front：输出队首元素，队首不出队。若队列为空，输出"empty"(不含引号)。
pop：输出队首元素，且队首出队。若队列为空，输出"empty"(不含引号)。
输入描述：
第一行输入两个整数
表示循环队列可利用的空间大小和操作次数。
接下来的q行，每行一个字符串，表示一个操作。保证操作是题目描述中的一种。
"""
import sys
l, num= input().split(" ")
stack1 = []
stack2 = []
for i in range(int(num)):
    ipt = input().split(" ")
    if ipt[0]=="push":
        if (len(stack1)+len(stack2))>=int(l):
            print("full")
        else:    
            stack1.append(ipt[1])
    elif ipt[0]=="pop":
        if not stack2:
            for i in range(len(stack1)):
                stack2.append(stack1.pop())
        if not stack2:
            print("empty")
        else:
            print(stack2.pop())
    elif ipt[0]=="front":
        if not stack2:
            for i in range(len(stack1)):
                stack2.append(stack1.pop())
        if not stack2:
            print("empty")
        else:
            print(stack2[-1])
