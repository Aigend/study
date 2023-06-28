"""
描述
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
数据范围:
\ \text{s.length}\le 40000 s.length≤40000
示例1
输入：
"abcabcbb"
复制
返回值：
3
复制
说明：
因为无重复字符的最长子串是"abc"，所以其长度为 3。 
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def findUnsortedSubarray(self , nums: List[int]) -> int:
        # write code here
