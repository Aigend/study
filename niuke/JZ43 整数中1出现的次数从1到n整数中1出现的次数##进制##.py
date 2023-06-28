
描述
输入一个整数 n ，求 1～n 这 n 个整数的十进制表示中 1 出现的次数
例如， 1~13 中包含 1 的数字有 1 、 10 、 11 、 12 、 13 因此共出现 6 次

注意：11 这种情况算两次

class Solution:
    def NumberOf1Between1AndN_Solution(self , n: int) -> int:
        # write code here
        res = 0
        for i in range(n+1):
            j = i
            while j > 0:
                if j % 10 == 1:
                    res += 1
                j = j // 10
        return res
