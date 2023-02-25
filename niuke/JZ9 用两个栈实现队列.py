# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ9 用两个栈实现队列.py
# @Date    : 2022/08/08:22:40
# @Author  : jinwenlong@oppo.com
# -*- coding:utf-8 -*-
class Solution:
    """

    实现队列，先进先出

    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()