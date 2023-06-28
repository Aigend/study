描述
假设你有一个数组prices，长度为n，其中prices[i]是某只股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
1. 你可以多次买卖该只股票，但是再次购买前必须卖出之前的股票
2. 如果不能获取收益，请返回0
3. 假设买入卖出均无手续费
输入：
[8,9,2,5,4,7,1]

返回值：
7

说明：
在第1天(股票价格=8)买入，第2天(股票价格=9)卖出，获利9-8=1
在第3天(股票价格=2)买入，第4天(股票价格=5)卖出，获利5-2=3
在第5天(股票价格=4)买入，第6天(股票价格=7)卖出，获利7-4=3
总获利1+3+3=7，返回7     

class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        if len(prices)<2:return 0
        #用dp[i][0]表示第i天不持股到该天为止的最大收益，
        #dp[i][1]表示第i天持股，到该天为止的最大收益
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        return dp[len(prices)-1][0]