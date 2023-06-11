"""
描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        # 运算超时
        # if number <= 1:
        #     return 1
        # return self.jumpFloor(number-1) + self.jumpFloor(number-2)
        m = {1: 1, 2:2}
        def jump(m, n):
            if n not in m:
                m[n] = jump(m, n-1) + jump(m, n - 2)
            return m[n]
        jump(m, number)
        return m[number]
if __name__ == '__main__':
    print(Solution().jumpFloor(4))