
# @File    : BM93 盛水最多的容器.py
# @Date    : 2022/06/30:0:15

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # write code here
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[right], height[left]) * (right - left), result)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


if __name__ == '__main__':
    print(Solution().maxArea([1, 7, 3, 2, 4, 5, 8, 2, 7]))
    print(Solution().maxArea([5, 4, 3, 2, 1, 5]))
    print(Solution().maxArea([2, 2]))
    print(Solution().maxArea([]))
