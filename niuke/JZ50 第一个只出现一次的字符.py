"""
描述
在一个长为 字符串中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        temp = {}
        for i in str:
            temp[i] = temp.get(i, 0)+1
        for i, k in enumerate(str):
            if temp[k]==1:
                return i
        return -1
