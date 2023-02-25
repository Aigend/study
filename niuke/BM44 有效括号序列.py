# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM44 有效括号序列.py
# @Date    : 2022/07/25:22:55
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s):
        # write code here
        stack = []
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        else:
            stack = []
            dict = {'(': ')', '[': ']', '{': '}'}
            for i in s:
                if i in dict:
                    stack.append(dict.get(i))
                else:
                    if stack and stack.pop() == i:
                        continue
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))