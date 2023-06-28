"""
请你实现一个队列。
操作：
push x：将 x 加入队尾，保证 x 为 int 型整数。
pop：输出队首，并让队首出队
front：输出队首：队首不出队
输出描述：
如果操作为push，则不输出任何东西。
如果为另外两种，若队列为空，则输出 "error“
否则按对应操作输出。
import sys
num= int(input())
stack1 = []
stack2 = []
for i in range(num):
    ipt = input().split(" ")
    if ipt[0]=="push":
        stack1.append(ipt[1])
    elif ipt[0]=="pop":
        if not stack2:
            for i in range(len(stack1)):
                stack2.append(stack1.pop())
        if not stack2:
            print("error")
        else:
            print(stack2.pop())
    elif ipt[0]=="front":
        if not stack2:
            for i in range(len(stack1)):
                stack2.append(stack1.pop())
        if not stack2:
            print("error")
        else:
            print(stack2[-1])
