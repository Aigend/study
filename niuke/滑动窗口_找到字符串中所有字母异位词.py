"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指字母相同，但排列不同的字符串。

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

如果做过类似题目，会第一时间想到双指针+字典的方式进行顺序比较。

1.维护一个ascii_lowercase为key的全零字典
2.根据p生成待匹配的字典信息dict_p
3.同理创建针对s的ascii_lowercase为key的全零字典
4.创建双指针，right从s[0]出发每次添加至tmp字典
5.当左右指针差距小于len§时，left指针不动
6.当左右指针差距等于len§时开始正式的对比操作，并每次匹配后left+=1
7.如果tmp等于dict_p,则将left指针添加入ret。
8.如果不匹配，删除掉左指针对应的字母。
9.right+=1
10.当right指针走至s末尾结束判断。

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        k_dict = {}.fromkeys(ascii_lowercase, 0)
        for i in p:
            k_dict[i] += 1
        tmp = {}.fromkeys(ascii_lowercase, 0)
        left = right = 0
        while right < len(s):
            tmp[s[right]] += 1
            if tmp == k_dict:
                ret.append(left)
            if right - left + 1 == len(p):
                tmp[s[left]] -= 1
                left += 1
            right += 1
        return ret
