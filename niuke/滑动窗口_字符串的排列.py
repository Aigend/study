"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
"""


# 排列关系如何处理？
# 用 collections.Counter() 实现对数组中元素个数的统计

import collections 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        s1_count = collections.Counter(s1)
        window_count = collections.Counter()
        window_size = len(s1)

        while right < len(s2):
            window_count[s2[right]] += 1
            # 窗口变小
            if right - left + 1 >= window_size:
                if window_count == s1_count:
                    return True
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            right += 1
        return False