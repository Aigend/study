描述
你是一个经验丰富的小偷，准备偷沿湖的一排房间，每个房间都存有一定的现金，为了防止被发现，你不能偷相邻的两家，
即，如果偷了第一家，就不能再偷第二家，如果偷了第二家，那么就不能偷第一家和第三家。沿湖的房间组成一个闭合的圆形，
即第一个房间和最后一个房间视为相邻。
给定一个长度为n的整数数组nums，数组中的元素表示每个房间存有的现金数额，请你计算在不被发现的前提下最多的偷窃金额。

这道题是环形，第一家和最后一家是相邻的，既然如此，在原先的方案中第一家和最后一家不能同时取到。
具体做法：
step 1：使用原先的方案是：用dp[i]表示长度为i的数组，最多能偷取到多少钱，
		只要每次转移状态逐渐累加就可以得到整个数组能偷取的钱。
step 2：（初始状态） 如果数组长度为1，只有一家人，肯定是把这家人偷了，收益最大，因此dp[1]=nums[0]。
step 3：（状态转移） 每次对于一个人家，我们选择偷他或者不偷他，如果我们选择偷那么前一家必定不能偷，
		因此累加的上上级的最多收益，
		同理如果选择不偷他，那我们最多可以累加上一级的收益。
		因此转移方程为dp[i]=max(dp[i−1],nums[i−1]+dp[i−2])。这里的i在dp中为数组长度，在nums中为下标。
step 4：此时第一家与最后一家不能同时取到，那么我们可以分成两种情况讨论：
情况1：偷第一家的钱，不偷最后一家的钱。初始状态与状态转移不变，只是遍历的时候数组最后一位不去遍历。
情况2：偷最后一家的请，不偷第一家的钱。初始状态就设定了dp[1]=0，
	  第一家就不要了，然后遍历的时候也会遍历到数组最后一位。

class Solution:
    def rob(self , nums: List[int]) -> int:
        #dp[i]表示长度为i的数组，最多能偷取多少钱
        dp1 = [0 for i in range(len(nums) + 1)] 
        #选择偷了第一家
        dp1[1] = nums[0] 
        #最后一家不能偷
        for i in range(2, len(nums)): 
            #对于每家可以选择偷或者不偷
            dp1[i] = max(dp1[i - 1], nums[i - 1] + dp1[i - 2]) 
        res = dp1[len(nums) - 1]; 
        #第二次循环
        dp2 = [0 for i in range(len(nums) + 1)] 
        #不偷第一家
        dp2[1] = 0 
        #可以偷最后一家
        for i in range(2, len(nums) + 1): 
            #对于每家可以选择偷或者不偷
            dp2[i] = max(dp2[i - 1], nums[i - 1] + dp2[i - 2]) 
            #选择最大值
        return max(res, dp2[len(nums)]) 


/*
当前家不偷或偷
当前不偷所获最大利润 = max(前一天不偷，前一天偷)；
dp[i][0] = max(dp[i-1][0],dp[i-1][1]);
当前偷所获最大利润 = 前一天没偷 + 今日所得
dp[i][1] = dp[i-1][0] + nums[i];

环形问题，分两种情况讨论：
第一种情况，偷或不偷第一家，确保不偷最后一家；
第二种情况，确保不偷第一家，最后一家偷或不偷。
*/
int max(int a, int b){
    if(a>b) return a;
    else return b;
}

int rob(int* nums, int numsLen ) {
    int dp[numsLen][2];
    memset(dp,0,sizeof(dp));
    //第一种情况，偷或不偷第一家，不偷最后一家
    dp[0][0] = 0;
    dp[0][1] = nums[0];
    for(int i = 1; i < numsLen-1; i++){
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]);
        dp[i][1] = dp[i-1][0] + nums[i];
    }
    int ret1 = max(dp[numsLen-2][0],dp[numsLen-2][1]);
    //第二种情况，不偷第一家，最后一家偷或不偷。
    memset(dp,0,sizeof(dp));
    dp[0][0] = 0;
    dp[0][1] = 0;
    for(int i = 1; i < numsLen; i++){
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]);
        dp[i][1] = dp[i-1][0] + nums[i];
    }
    int ret2 = max(dp[numsLen-1][0],dp[numsLen-1][1]);
    return max(ret1,ret2);
}
 
# 自己实际提交的代码
class Solution:
    def rob(self , nums: List[int]) -> int:
        # write code here
        dp= [[0, 0] for _ in range(len(nums)+1)]
        dp[1][0]=0
        dp[1][1]=nums[0]
        ret = 0
        for i in range(2, len(nums)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1])
            dp[i][1]= dp[i-1][0]+nums[i-1]
        ret = max(dp[len(nums)-1][0], dp[len(nums)-1][1])

        dp[1][1]=0
        for i in range(2, len(nums)+1):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1])
            dp[i][1]= dp[i-1][0]+nums[i-1]

        ret = max(dp[len(nums)][0], dp[len(nums)][1], ret)
        
        return ret