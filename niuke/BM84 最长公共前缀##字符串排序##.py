
# @File    : BM84 最长公共前缀.py
# @Date    : 2022/07/03:21:12
"""
描述
给你一个大小为 n 的字符串数组 strs ，其中包含n个字符串 , 
编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀。
"""
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