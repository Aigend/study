# @File    : BM60 括号生成.py
# @Date    : 2022/09/05:22:56

"""
    描述
    给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
    例如，给出n=3，解集为：
    "((()))", "(()())", "(())()", "()()()", "()(())"
    
    数据范围：0 \le n \le 100≤n≤10
    要求：空间复杂度 O(n)O(n)，时间复杂度 O(2^n)O(2 n)
"""
class Solution:
    def generateParenthesis(self , n: int) -> List[str]:
        # write code here
        result = []
        def recursive(l, r, s):
            if len(s) == 2 * n:
                result.append(s)
            if l < n:
                recursive(l+1, r, s+"(")
            if r < l:
                recursive(l, r+1, s+")")
        recursive(0,0,"")
        return result