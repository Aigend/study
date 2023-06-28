描述
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。传入的字符串可能有以下部分组成:
1.若干空格
2.（可选）一个符号字符（'+' 或 '-'）
3. 数字，字母，符号，空格组成的字符串表达式
4. 若干空格

转换算法如下:
1.去掉无用的前导空格
2.第一个非空字符为+或者-号时，作为该整数的正负号，如果没有符号，默认为正数
3.判断整数的有效部分：
3.1 确定符号位之后，与之后面尽可能多的连续数字组合起来成为有效整数数字，如果没有有效的整数部分，那么直接返回0
3.2 将字符串前面的整数部分取出，后面可能会存在存在多余的字符(字母，符号，空格等)，这些字符可以被忽略，它们对于函数不应该造成影响
3.3  整数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231的整数应该被调整为 −231 ，大于 231 − 1 的整数应该被调整为 231 − 1
4.去掉无用的后导空格

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return int整型
#
class Solution:
    def StrToInt(self , s: str) -> int:
        # write code here
        res = 0
        index = 0
        #去掉前导空格
        s = s.strip()
        #去掉空格就什么都没有了
        n = len(s)
        if s == "":
            return 0
        sign = 1
        #处理第一个符号是正负号的情况
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            index += 1
            sign = -1
        #去掉符号就什么都没有了
        if index == n:
            return 0
        while index < n:
            c = s[index]
            #后续非法字符，截断
            if c < '0' or c > '9': 
                break
            #转数字
            res = res * 10 + sign * ((int)(c) - (int)('0'))
            index += 1
        #输出处理越界
        return min(max(res, -2 ** 31), 2 ** 31 - 1)
