# @File    : BM56 有重复项数字的全排列.py
# @Date    : 2022/09/05:21:29

from copy import copy
from collections import Counter


class Solution:
    def permuteUnique(self, num):
        # write code here
        result = []
        track = []
        def trackback(track, counter):
            if len(track) == len(num):
                result.append(copy(track))
            for n in counter:
                if counter[n]:
                    track.append(n)
                    counter[n] -= 1
                    trackback(track, counter)
                    track.pop()
                    counter[n] += 1

        trackback(track, Counter(num))
        return result

print(Solution().permuteUnique([1, 1, 2]))