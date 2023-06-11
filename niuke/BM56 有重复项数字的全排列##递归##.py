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
    
import copy
class Solution:
    def permuteUnique(self , num: List[int]) -> List[List[int]]:
        # write code here
        n = len(num)
        res = []
        tmp = []
        m = {}
        num.sort()
        for k in num:
            m[k]= m.get(k, 0) + 1
        def dfs(n, num, tmp, res, m):
            if len(tmp) == n:
                res.append(copy.copy(tmp))
                return
            print(m, tmp)
            for k, v in m.items():
                if v > 0:
                    tmp.append(k)
                    print(v, m[k])
                    m[k] = v-1  # 这里写成 v -1 就不行，没太明白
                    dfs(n, num, tmp, res, m)
                    tmp.pop()
                    m[k] = v+ 1
        dfs(n, num, tmp, res, m)
        return res
    
print(Solution().permuteUnique([1, 1, 2]))
