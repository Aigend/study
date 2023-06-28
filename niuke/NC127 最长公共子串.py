"""
描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。 

数据范围： 1 \le |str1|,|str2| \le 50001≤∣str1∣,∣str2∣≤5000
要求： 空间复杂度 O(n^2)O(n 
2
 )，时间复杂度 O(n^2)O(n 
2
 )
示例1
输入：
"1AB2345CD","12345EF"
复制
返回值：
"2345"
复制
备注：
1 \leq |str_1|, |str_2| \leq 5\,0001≤∣str 
1
​
 ∣,∣str 
2
​
 ∣≤5000
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here