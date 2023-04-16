# @File    : BM55 没有重复项数字的全排列.py
# @Date    : 2022/09/05:20:09

from copy import copy
class Solution:
    def permute(self , num):
        # write code here
        result = []
        track = []
        def trackback(track, num, result):
            if len(track) == len(num):
                result.append(copy(track))
                return
            for i in num:
                if i in track:
                    continue
                track.append(i)
                trackback(track, num, result)
                track.pop()
        trackback(track, num, result)
        return result

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))