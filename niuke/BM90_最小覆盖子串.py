BM90_最小覆盖子串

描述

给出两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串。

注意：
如果 s 中没有包含 t 中所有字符的子串，返回空字符串 “”；
满足条件的子串可能有很多，但是题目保证满足条件的最短的子串唯一。

class Solution:
    #检查是否有小于0的
    def check(self, hash:dict()): 
        for key, value in hash.items():
            if value < 0:
                return False
        return True

    def minWindow(self , S: str, T: str) -> str:
        cnt = len(S) + 1
        #记录目标字符串T的字符个数
        hash = dict() 
        for i in range(len(T)):
            if T[i] in hash:
                #初始化哈希表都为负数，找的时候再加为正
                hash[T[i]] -= 1 
            else:
                hash[T[i]] = -1
        slow = 0
        fast = 0
        left = -1
        #记录左右区间
        right = -1 
        while fast < len(S):
            c = S[fast]
            #目标字符匹配+1
            if c in hash:
                hash[c] += 1
            #没有小于0的说明都覆盖了，缩小窗口
            while (Solution.check(self, hash)) :   
                #取最优解
                if  cnt > fast - slow + 1: 
                    cnt = fast - slow + 1
                    left = slow
                    right = fast
                c = S[slow]
                if c in hash:
                    #缩小窗口的时候减1
                    hash[c] -= 1 
                #窗口缩小
                slow += 1      
            fast += 1
        #找不到的情况
        if left == -1:    
            return ""
        return S[left:right+1]
