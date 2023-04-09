给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
# 暴力解题
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 一个一个的遍历
        result = 1
        res = s[0]
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                left = i
                right = j
                while left < right:
                    if s[left]==s[right]:
                        left += 1
                        right -= 1
                    else:
                        break
                if left >= right:
                    if j - i + 1>result:
                        result = j - i + 1
                        res = s[i:j+1]

            if result == len(s):
                res = s
                break
        return res  
# 中心扩展，其实本质也是暴力解题
# 动态规划，没看懂
