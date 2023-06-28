"""
描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
#

import math
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Sum_Solution(self , n: int) -> int:
        # write code here
        # return sum(n)
        res = int((math.pow(n, 2) + n))>>1
        return res
