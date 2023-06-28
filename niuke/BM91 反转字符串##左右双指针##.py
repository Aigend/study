# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM91 反转字符串.py
# @Date    : 2022/06/29:23:45
# @Author  : jinwenlong@oppo.com

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self , str: str) -> str:
        # write code here
#         return str[::-1]
        str = list(str)
        left = 0
        right = len(str) - 1
        while left < right:
            str[left], str[right] = str[right], str[left]
            left += 1 # 这里调试的时候漏写
            right -= 1
        return "".join(str)

if __name__ == '__main__':
    print(Solution().solve("adba"))