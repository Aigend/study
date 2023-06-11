# @File    : BM55 没有重复项数字的全排列.py
# @Date    : 2022/09/05:20:09
import copy
from collections import Counter
class Solution:
    def permute(self , num: List[int]) -> List[List[int]]:
        # write code here
        # 第一种方法
        # res = []
        # tmp = []
        # s = set()
        # n = len(num)
        # def dfs(n, num, s, tmp, res):
        #     if len(tmp) == n:
        #         res.append(copy.copy(tmp))
        #         return
        #     for k in num:
        #         if k in s:
        #             continue
        #         tmp.append(k)
        #         s.add(k)
        #         dfs(n, num, s,tmp, res)
        #         tmp.pop()
        #         s.remove(k)
        # dfs(n, num, s, tmp, res)
        # return res

        # 第二种
        res = []
        tmp = []
        n = len(num)
        num.sort()
        counter = Counter(num)
        def dfs(res, tmp, n, counter):
            if len(tmp) == n:
                res.append(copy.copy(tmp))
                return
            for v in counter:
                if counter[v]:
                    tmp.append(v)
                    counter[v] -= 1
                    dfs(res, tmp, n, counter)
                    tmp.pop()
                    counter[v] += 1
        dfs(res, tmp, n, counter)
        return res
