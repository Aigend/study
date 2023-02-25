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
        result = self.GuiBingSort(arr, 0, n-1)
        return result

    def GuiBingSort(self, arr, left, right):
        if left >= right:
            return [arr[left]]
        mid = left + (right-left)//2
        res_left = self.GuiBingSort(arr, left, mid)
        res_right = self.GuiBingSort(arr, mid+1, right)
        temp = []
        i = 0
        j = 0
        while i < len(res_left) and j < len(res_right):
            if res_left[i] < res_right[j]:
                temp.append(res_left[i])
                i+=1
            else:
                temp.append(res_right[j])
                j+=1
        if i < len(res_left):
            temp.extend(res_left[i:]) 
        elif j < len(res_right):
            temp.extend(res_right[j:])
        return temp
