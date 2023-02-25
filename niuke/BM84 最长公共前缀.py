# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM84 最长公共前缀.py
# @Date    : 2022/07/03:21:12
# @Author  : jinwenlong@oppo.com
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # write code here
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) > 1:
            strs.sort(key=len, reverse=False)
            result = []
            flag = False
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[j][i] != strs[0][i]:
                        flag = True
                        break
                else:
                    result.append(strs[0][i])
                if flag:
                    break
            return "".join(result)



