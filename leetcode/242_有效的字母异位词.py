242_有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        req = {}
        if len(s)!=len(t):return False
        for i in range(len(s)):
            res[s[i]]=res.get(s[i],0)+1
            req[t[i]]=req.get(t[i], 0)+1
        for k, v in res.items():
            if req.get(k)!=v:
                return False
        return True
