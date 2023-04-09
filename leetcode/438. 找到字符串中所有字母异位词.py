给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        if len(s)<len(p):
            return result
        req = {}
        for i in p:
            req[i]=req.get(i, 0)+1
        res = {}
        # 这里思路错了，需要使用滑动窗口的方法
        # for j in range(len(s)):
        #     res[s[j]]=res.get(s[j], 0)+1
        #     if self.isValid(res, req):
        #         result.append(j+1-len(p))
        # 滑动窗口
        for i in range(len(p)):
            res[s[i]]=res.get(s[i], 0)+1
        if self.isValid(res, req):result.append(0)
        for i in range(len(p), len(s)):
            res[s[i]]=res.get(s[i], 0)+1
            res[s[i-len(p)]] -= 1
            if res[s[i-len(p)]] == 0:  # 这里要加上value变为0时，删掉key值
                del res[s[i-len(p)]]
            if self.isValid(res, req):
                result.append(i-len(p)+1)
        return result


    def isValid(self, s, p):
        if len(s)!=len(p):
            return False
        for k, v in s.items():
            if p.get(k) != v:
                return False
        return True
