描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度
输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度
import sys

s = input()
max_l = 1
for i in range(len(s)):
    for j in range(len(s)-1, i, -1):
        k_l = i
        k_r = j
        while s[k_l]==s[k_r]:
            if k_l>=k_r:
                break
            else:
                k_l+=1
                k_r-=1
        if k_l>=k_r:
            max_l = max(max_l, j-i+1)
            break
    if max_l == len(s):
        break
print(max_l)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_ = 1
        max_start = 0
        length = len(s)
        for i in range(length): # odd
            for k in range(2):
                k_l = i-k # 0 代表偶数，1代表奇数 
                k_r = i+1
                while(k_l>=0 and k_r<length and s[k_l]==s[k_r]):
                    k_l -= 1
                    k_r += 1
                if max_ < k_r - k_l-1:
                    max_ = k_r - k_l-1
                    max_start = k_l+1
        return s[max_start:max_start+max_]               
