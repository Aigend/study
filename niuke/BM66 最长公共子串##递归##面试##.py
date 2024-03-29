描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。 

class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        #dp[i][j]表示到str1第i个个到str2第j个为止的公共子串长度
        dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
        max = 0
        pos = 0
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                #如果该两位相同
                if str1[i - 1] == str2[j - 1]: 
                    #则增加长度
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else: 
                    #该位置为0
                    dp[i][j] = 0 
                #更新最大长度
                if dp[i][j] > max: 
                    max = dp[i][j]
                    pos = i - 1
        return str1[pos - max + 1: pos + 1]
