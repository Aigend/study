"""
描述
给定一个十进制数 M ，以及需要转换的进制数 N 。将十进制数 M 转化为 N 进制数。

当 N 大于 10 以后， 应在结果中使用大写字母表示大于 10 的一位，如 'A' 表示此位为 10 ， 'B' 表示此位为 11 。

若 M 为负数，应在结果中保留负号。

数据范围： M <= 10^8 , 2 \le N \le 16M<=10 
8
 ,2≤N≤16
要求：空间复杂度O(log_MN)O(log 
M
​
 N)，时间复杂度 O(log_MN)O(log 
M
​
 N)
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 进制转换
# @param M int整型 给定整数
# @param N int整型 转换到的进制
# @return string字符串
#
class Solution:
    def solve(self , M: int, N: int) -> str:
        # write code here
        if N == 10:
            return M
        fushu = False
        if M < 0:
            fushu = True
            M = abs(M)
        temp = []
        key = {
            10:"A",
            11:"B",
            12:"C",
            13:"D",
            14:"E",
            15:"F",
        }
        while M // N != 0 :
            yushu = M % N
            if N > 10 and yushu >= 10:
                yushu = key.get(yushu)
            temp.append(str(yushu))
            M = M//N
        yushu = M % N
        if N > 10 and yushu >= 10:
            yushu = key.get(yushu)
        temp.append(str(yushu))
        result = "".join(temp[::-1])
        if fushu:
            return "-" + result
        return result