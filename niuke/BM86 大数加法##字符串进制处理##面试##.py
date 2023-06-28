
# @File    : BM86 大数加法##字符串进制处理##面试##.py
# @Date    : 2022/07/04:23:08
"""
描述
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。

算法流程： 
    设定 i，j 两指针分别指向 s，t 尾部，模拟人工加法；
    计算进位： 计算 carry = tmp // 10，代表当前位相加是否产生进位；
    添加当前位： 计算 tmp = n1 + n2 + carry，并将当前位 tmp % 10 添加至 res 头部；
    索引溢出处理： 当指针 i或j 走过数字首部后，给 n1，n2 赋值为 0，相当于给 s，t 中长度较短的数字前面填 0，以便后续计算。
    当遍历完 s，t 后跳出循环，并根据 carry 值决定是否在头部添加进位 1，最终返回 res 即可
"""
class Solution:
    def solve(self, s: str, t: str) -> str:
        # write code here
        # return str(int(s) + int(t))

        res = ""
        i, j, carry = len(s) - 1, len(t) - 1, 0
        while i >= 0 & j >= 0:
            n1 = int(s[i]) if i >= 0 else 0
            n2 = int(t[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


if __name__ == '__main__':
    print(Solution().solve("123", "49"))
    # print(False & False)
