709_转换成小写字母.py

给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
class Solution:
    def toLowerCase(self, s: str) -> str:
        # res = []
        # for v in s:
        #     res.append(v.lower())
        # return "".join(res)
        return s.lower()
