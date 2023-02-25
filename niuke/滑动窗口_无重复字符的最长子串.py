"""
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
"""
# 双指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        window = {}

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            # 缩减窗口
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            # 维护一个最大值
            result = max(result, right - left + 1)
            right += 1
        return result
"""

def maxLength(arr: List[int]) -> int:
    # write code here
    left = 0
    right = 0
    result = 0
    temp = {}
    for ind, val in enumerate(arr):
        if val not in temp.keys():
            right += 1
            temp[val] = ind
        else:
            result = max(result, right-left)
            left = temp.get(val) + 1
    return result

if __name__ == '__main__':
	print(maxLength(list("1234")))
