
# @File    : BM83 字符串变形.py
# @Date    : 2022/07/03:20:55
"""
描述
对于一个长度为 n 字符串，我们需要对它做一些变形。

首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把这个字符串中由空格隔开的单词反序，

同时反转每个字符的大小写。

比如"Hello World"变形后就变成了"wORLD hELLO"。
"""

class Solution:
    def trans(self, s: str, n: int) -> str:
    # write code here
        s = s.split(" ")
        result = []
        for i in range(len(s)-1, -1, -1):
            result.append("".join([s[i][j].upper() if s[i][j].islower() else s[i][j].lower() for j in range(len(s[i]))]))
        return " ".join(result)