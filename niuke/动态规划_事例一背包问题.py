"""
0-1背包问题：给定n中物品和一个容量为C的背包，物品i的重量是wi，其价值为vi。

问：应该如何选择装入背包的物品，使得装入背包的物品的总结之最大？

分析一波：面对每个物品，我们只有选择拿取或者不拿两种选择，不能选择装入某个物品的一部分，也不能装入同一个物品多次。

解决办法：
声明一个大小为m[n][c]的二维数组，m[i][j]表示在面对第i个物品，且背包容量为j时所能获得的最大价值。
那么我们可以很容易分析出m[i][j]的计算方法。

j<w[i]的情况，这时候背包容量不足以放下第i个物品，只能选择不拿
m[i][j] = m[i-1][j]
j>=w[i]的情况，这时背包容量可以放下第i件物品，我们就要考虑拿这件物品是否能获取更大的价值。
如果拿取，m[i][j]=m[i-1][j-w[i]]+v[i]，这里的m[i-1][j-w[i]]指的就是考虑了i-1个物品，背包容量为j-w[i]时的最大价值，也是相当于为第i个物品腾出了w[i]的空间。
如果不拿，m[i][j]=m[i-1][j]，同(1)
最终拿还是不拿，取决于这两种情况那种价值最大。

如果我们最终还需要获取到拿了哪些物品，需另起一个x[]数组，x[i]=0表示不拿，x[i]=1表示拿。
m[n][c]为最优值，如果m[n][c]=m[n-1][c]，说明有没有第n个物品都一样，则x[n]=0;
否则x[1]=1，则由x[n-1][c-w[i]]继续构造最优解。依次类推，可构造出所有最优解。
"""


import sys

c = int(sys.stdin.readline())
w = [int(num) for num in sys.stdin.readline().strip.split()]
v = [int(val) for val in sys.stdin.readline().strip.split()]
n = len(w)

dp = [[0 for _ in range(c+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, c+1):
        dp[i][j]= dp[i-1][j]
        if j >= w[j-1]:
            dp[i][j]= max(dp[i-1][j-w[i-1]]+v[i-1], dp[i-1][j])
sys.stdout.write(str(dp[n][c]))

def track(d, c, w):
    # d是dp数组
    # c是背包容量
    # w是物品的数据
    x = []
    for i in range(len(w), 1, -1):
        if d[i][c] != d[i-1][c]:
            x.append(w[i-1])
            c = c - w[i-1]

    # 拿一个物品时，价值最大的这个值肯定是需要的
    if d[1][c] > 0:
        x.append(w[0])

    return x

print(track(dp,c,w))