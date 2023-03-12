"""

平时我们习惯将表达式写成 (1 + 2) * (3 + 4)，加减乘除等运算符写在中间，因此称呼为中缀表达式。
而波兰表达式的写法为 (* (+ 1 2) (+ 3 4))，将运算符写在前面，因而也称为前缀表达式。
逆波兰表达式的写法为 ((1 2 +) (3 4 +) *)，将运算符写在后面，因而也称为后缀表达式。
波兰表达式和逆波兰表达式有个好处，就算将圆括号去掉也没有歧义。上述的波兰表达式去掉圆括号，变为 * + 1 2 + 3 4。
逆波兰表达式去掉圆括号，变成 1 2 + 3 4 + * 也是无歧义并可以计算的。事实上我们通常说的波兰表达式和逆波兰表达式就是去掉圆括号的。
而中缀表达式，假如去掉圆括号，将 (1 + 2) * (3 + 4) 写成 1 + 2 * 3 + 4，就改变原来意思了。
输入：
["2","1","+","4","*"]
返回值：
12
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param tokens string字符串一维数组 
# @return int整型
#
class Solution:
    def evalRPN(self , tokens: List[str]) -> int:
        # write code here
        stack = []
        for val in tokens:
            # if val.isdigit():# 这里有问题。isdigit只对0h和正数有效
            #     stack.append(val)
            #     print(stack)
            if val not in "+-*/":
                stack.append(val)
            elif val in ["+", "*"]:
                stack.append(str(eval(stack.pop() + val + stack.pop())))
            elif val == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(str(int(val2)-int(val1)))
            elif val == "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if val1<0 or val2<0:
                    stack.append(str(int(int(val2)/int(val1))))
                else:
                    stack.append(str(int(val2)//int(val1)))
        return int(stack[-1])
