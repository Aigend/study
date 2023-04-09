49_字母异位词分组

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 对每个单词中的字母顺序进行排序
        result = {}
        for s in strs:
            s_ = "".join(sorted(s)) # 排序这一步很重要，不然不同顺序的异位词无法区分
            if s_ not in result:
                result[s_]=[s]
            else:
                result[s_].append(s)
        return list(result.values()) # 字典的value转成list
