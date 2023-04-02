"""
描述
实现函数 double Power(double base, int exponent)，求base的exponent次方。

注意：
1.保证base和exponent不同时为0。
2.不得使用库函数，同时不需要考虑大数问题
3.有特殊判题，不用考虑小数点后面0的位数。"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param base double浮点型 
# @param exponent int整型 
# @return double浮点型
#
import math
class Solution:
    def Power(self , base: float, exponent: int) -> float:
        # write code here
        # return math.pow(base,exponent)
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        result = 1
        for i in range(exponent):
            result *= base
        return result
