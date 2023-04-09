如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
class Solution:
    def isPalindrome(self, s: str):
        # left = 0
        # right = len(s)-1
        # while left < right:
        #     while left < right and not s[left].isalnum() and not s[left].isnumeric():
        #         left += 1
        #     while right > left and not s[right].isalnum() and not s[right].isnumeric():
        #         right -= 0
        #     if left < right:
        #         if s[left].lower == s[right].lower():
        #             left += 1
        #             right -= 1
        #         else:
        #             return False
        #
        # return True
        tmp = []
        for v in s:
            if v.isalnum() or v.isnumeric():
                tmp.append(v.lower())
        left = 0
        right = len(tmp) -1
        while left < right:
            if tmp[left] == tmp[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
