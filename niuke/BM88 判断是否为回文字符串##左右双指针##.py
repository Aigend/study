# @File    : BM88 判断是否为回文字符串.py
# @Date    : 2022/06/28:23:39

class Solution:
    def judge(self, str: str) -> bool:
        left = 0
        right = len(str) - 1
        while left < right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
            # 121
            # 1221
        return True
# write code here
