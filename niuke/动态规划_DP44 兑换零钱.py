"""
描述
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
如果无解，请返回-1.

数据范围：数组大小满足 0 \le n \le 100000≤n≤10000 ， 数组中每个数字都满足 0 < val \le 100000<val≤10000，0 \le aim \le 50000≤aim≤5000

要求：时间复杂度 O(n \times aim)O(n×aim) ，空间复杂度 O(aim)O(aim)。
输入描述：
第一行给定两个正整数分别是 n 和 aim 分别表示数组 arr 的长度和要找的钱数。
第二行给定 n 个正整数表示 arr 数组中的所有元素
输出描述：
输出组成 aim 的最少货币数
"""
import sys
n, aim = map(int, input().split())
v = list(map(int, input().split()))
dp = [sys.maxsize] * (aim + 1)
dp[0] = 0
for i in range(n):
    for j in range(aim+1):
        if j >= v[i]:
            dp[j] = min(dp[j], dp[j-v[i]] + 1)
print(dp[-1] if dp[-1] != sys.maxsize else -1)
