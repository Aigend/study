"""
描述
给定一个长度为 n 的数组，请你编写一个函数，返回该数组按升序排序后的结果。

数据范围： 0 \le n \le 1\times10^30≤n≤1×10 
3
 ，数组中每个元素都满足 0 \le val \le 10^90≤val≤10 
9
 
要求：时间复杂度 O(n^2)O(n 
2
 )，空间复杂度 O(n)O(n)
进阶：时间复杂度 O(nlogn)O(nlogn)，空间复杂度 O(n)O(n)

注：本题数据范围允许绝大部分排序算法，请尝试多种排序算法的实现。
示例1
输入：
[5,2,3,1,4]
复制
返回值：
[1,2,3,4,5]
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    def MySort(self , arr: List[int]) -> List[int]:
        # write code here
        n = len(arr)
        for i in range(n-1):
            min_ind = i
            for j in range(i+1, n):
                if arr[min_ind]>arr[j]:
                    min_ind = j
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
        return arr