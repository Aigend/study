给你一个字符串 s，最多 可以从中删除一个字符。

请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        judge = lambda x: x == x[::-1]
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return judge(s[left: right]) or judge(s[left+1: right+1])  # 不匹配的时候就是去掉左边的，或者去掉右边的，看是否匹配
        return True
