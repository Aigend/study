# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : JZ5 替换空格.py
# @Date    : 2022/08/08:21:16
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串
#
class Solution:
    def replaceSpace(self , s: str) -> str:
        # write code here
        t = s.split(" ")
        return "%20".join(t)
    #         s.replaceAll(self, " ", "%20")