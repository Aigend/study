# @File    : BM58 字符串的排列.py
# @Date    : 2022/09/05:22:41
#
from collections import Counter
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        num = list(str)
        result = []
        track = []
        def trackback(track, counter):
            if len(track) == len(num):
                result.append("".join(track))
            for n in counter:
                if counter[n]:
                    track.append(n)
                    counter[n] -= 1
                    trackback(track, counter)
                    track.pop()
                    counter[n] += 1

        trackback(track, Counter(num))
        return result