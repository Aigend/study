# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM88 判断是否为回文字符串.py
# @Date    : 2022/06/28:23:39
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self, str: str) -> bool:
        left = 0
        right = len(str) - 1
        while left < right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
            # 121
            # 1221
        return True
# write code here
