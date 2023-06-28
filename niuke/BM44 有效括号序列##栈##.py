# python实现有效的括号判断##栈##

# 题目描述
# 给定一个只包括 '(',')','{','}','[',']'的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1

class Solution:
    def isValid(self, s):
        # write code here
        stack = []
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        else:
            stack = []
            dict = {'(': ')', '[': ']', '{': '}'}
            for i in s:
                if i in dict:
                    stack.append(dict.get(i))
                else:
                    if stack and stack.pop() == i:
                        continue
                    else:
                        return False
            if len(stack) == 0:
                return True
            else:
                return False


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))