# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM87 合并两个有序的数组.py
# @Date    : 2022/06/28:23:29
# @Author  : jinwenlong@oppo.com

#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:

    def merge(self, A, m, B, n):
        # write code here
        # A += [None] * n
        # print(A)
        merge = m + n - 1
        m = m - 1
        n = n - 1
        while m > -1 and n > -1:
            if A[m] < B[n]:
                A[merge] = B[n]
                merge -= 1
                n -= 1
            elif A[m] >= B[n]:
                A[merge] = A[m]
                merge -= 1
                m -= 1
        print(A)
        print(B[:n+1])
        if n > -1:
            for i in range(n+1):
                A[i] = B[i]
        print(A)
        return A

    def solution(self , A, m, B, n):
        # write code here
#         A += [None]*n
        """
        说明：
        A数组为[4,5,6]，B数组为[1,2,3]，
        后台程序会预先将A扩容为[4,5,6,0,0,0]，B还是为[1,2,3]，m=3，n=3，传入到函数merge里面，
        然后请同学完成merge函数，将B的数据合并A里面，最后后台程序输出A数组
        """
        merge = m + n -1
        m = m-1
        n = n -1
        while m >-1 and n > -1:
            if A[m] < B[n]:
                A[merge] = B[n]
                merge -= 1
                n -=1
            elif A[m] >= B[n]:
                A[merge] = A[m]
                merge -= 1
                m -= 1
        if n > -1:
            for i in range(n+1):
                A[i] = B[i]


if __name__ == '__main__':
    Solution().merge([4, 5, 6], 3, [1, 2, 3], 3)
