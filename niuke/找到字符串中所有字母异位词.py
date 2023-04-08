方法一：滑动窗口
思路

根据题目要求，我们需要在字符串 
�
s 寻找字符串 
�
p 的异位词。因为字符串 
�
p 的异位词的长度一定与字符串 
�
p 的长度相同，所以我们可以在字符串 
�
s 中构造一个长度为与字符串 
�
p 的长度相同的滑动窗口，并在滑动中维护窗口中每种字母的数量；当窗口中每种字母的数量与字符串 
�
p 中每种字母的数量相同时，则说明当前窗口为字符串 
�
p 的异位词。

算法

在算法的实现中，我们可以使用数组来存储字符串 
�
p 和滑动窗口中每种字母的数量。

细节

当字符串 
�
s 的长度小于字符串 
�
p 的长度时，字符串 
�
s 中一定不存在字符串 
�
p 的异位词。但是因为字符串 
�
s 中无法构造长度与字符串 
�
p 的长度相同的窗口，所以这种情况需要单独处理。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            
            if s_count == p_count:
                ans.append(i + 1)

        return ans
