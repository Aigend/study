"""
输入：s = 'abciiidef' k = 3（子串定长为3）
输出：3
解释：子字符串 'iii' 包含 3 个元音字母

"""

def countSub(s, k):
    if s == None or len(s) == 0 or len(s) < k:
        return 0
    
    # 元音字母哈希
    hashset = {'a', 'e', 'i', 'o', 'u'}
    res = 0
    count = 0
    for i in range(k):          # 窗口为 k
        if s[i] in hashset:
            count += 1
        res = max(res, count)
    for i in range(k, len(s)):
        if s[i-k] in hashset:   # 窗口右移
            count -= 1
        if s[i] in hashset:
            count += 1
        res = max(res, count)

    return res

s = 'abciiidef'   
k = 3
print(countSub(s, k))