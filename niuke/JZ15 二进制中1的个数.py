"""
描述
输入一个整数 n ，输出该数32位二进制表示中1的个数。其中负数用补码表示。
"""
class Solution:
    def NumberOf1(self , n: int) -> int:
        # write code here
        result = 0
        for i in range(32):
            # print(1<<i)
            if (n & (1 << i)) != 0:
                # print(result)
                result += 1
        return result
