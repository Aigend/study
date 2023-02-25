# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM86 大数加法.py
# @Date    : 2022/07/04:23:08
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s: str, t: str) -> str:
        # write code here
        # return str(int(s) + int(t))

        res = ""
        i, j, carry = len(s) - 1, len(t) - 1, 0
        while i >= 0 & j >= 0:
            n1 = int(s[i]) if i >= 0 else 0
            n2 = int(t[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


if __name__ == '__main__':
    print(Solution().solve("123", "49"))
    # print(False & False)
