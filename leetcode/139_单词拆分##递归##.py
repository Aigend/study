139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用

# 未全部通过，存在超时的情况，需要优化
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = False
        tmp = []
        wordDict = set(wordDict)

        def dfs(tmp, wordDict):
            nonlocal result
            res = "".join(tmp)
            if len(res) == len(s):
                if res == s:
                    result = True
            elif len(res) > len(s):
                return
            for i in wordDict:
                if not result:
                    tmp.append(i)
                    dfs(tmp, wordDict)
                    tmp.pop()
        dfs(tmp, wordDict)
        return result