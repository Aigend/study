描述
给定一个数组 A[0,1,...,n-1] ,请构建一个数组 B[0,1,...,n-1] ,其中 B 的元素 B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]（除 A[i] 以外的全部元素的的乘积）。程序中不能使用除法。（注意：规定 B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2]）
对于 A 长度为 1 的情况，B 无意义，故而无法构建，用例中不包括这种情况。
输入：
[1,2,3,4,5]
返回值：
[120,60,40,30,24]
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def multiply(self , A: List[int]) -> List[int]:
        # write code here
        B = [1 for _ in range(len(A))]
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        tmp = 1
        for i in range(len(A)-1, -1, -1):
            B[i] *= tmp
            tmp *= A[i]
        return B
