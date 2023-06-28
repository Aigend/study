"""
题解 | #有多少个不同的二叉搜索树#

思路：动态规划
1. 确定dp数组代表的含义
    dp[i]：有i个节点时的总共的二叉搜索树个数
2. 确定递推公式
    当有 i 个结点时，以 j 为头节点，左子树元素为 1~j-1（共 j-1 个节点），右子树元素为 j+1~i （共 i-j 个节点），
    故左子树的搜索二叉树个数为 dp[j-1]，右子树的搜索二叉树个数为 dp[i-j] ，此时搜索二叉树总的个数为 dp[j-1] * dp[i-j]
    故递推公式为：dp[i] = sum(dp[j-1] * dp[i-j])
3. 初始化
    要求累加值，所以 dp[i] 初始化值为0，当节点为0个或1个时，都只有1种方案
"""

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] += dp[j-1] * dp[i-j]
         
print(dp[n])