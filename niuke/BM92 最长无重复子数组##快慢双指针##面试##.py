# @File    : BM92 最长无重复子数组.py
# @Date    : 2022/06/29:23:48

from typing import List

class Solution:
    def maxLength(self , arr: List[int]) -> int:
        # write code here
        # 这里使用双指针
        m = set()
        left = 0
        right = 0
        result = 0
        for i in range(len(arr)):
            if arr[i] not in m:
                m.add(arr[i])
            else:
                result = max(len(m), result)
                print("#", m)
                while arr[left] != arr[i]:
                    print(arr[left])
                    m.remove(arr[left])
                    left += 1
                # m.remove(arr[left])
                left += 1
                # m.add(arr[i])
        return max(result, len(m))

if __name__ == '__main__':
    print(Solution().maxLength([1,3,4,5,2,5,3,5,3,6,5,2,1,3]))