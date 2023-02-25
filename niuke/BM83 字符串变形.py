# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM83 字符串变形.py
# @Date    : 2022/07/03:20:55
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @param n int整型
# @return string字符串
#


class Solution:
    def trans(self, s: str, n: int) -> str:
    # write code here
        s = s.split(" ")
        result = []
        for i in range(len(s)-1, -1, -1):
            result.append("".join([s[i][j].upper() if s[i][j].islower() else s[i][j].lower() for j in range(len(s[i]))]))
        return " ".join(result)


