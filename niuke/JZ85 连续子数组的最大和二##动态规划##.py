描述
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，找到一个具有最大和的连续子数组。
1.子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
2.如果存在多个最大和的连续子数组，那么返回其中长度最长的，该题数据保证这个最长的只存在一个
3.该题定义的子数组的最小长度为1，不存在为空的子数组，即不存在[]是某个数组的子数组
4.返回的数组不计入空间复杂度计算


可以用dp数组表示以下标i为终点的最大连续子数组和，
则每次遇到一个新的数组元素，连续的子数组要么加上变得更大，要么它本身就更大，因此状态转移为
dp[i]=max(dp[i−1]+array[i],array[i])，这是最基本的求连续子数组的最大和。

每次用left、right记录该子数组的起始，需要更新最大值的时候（要么子数组和更大，要么子数组和相等的情况下区间要更长）
顺便更新最终的区间首尾，这样我们的区间长度就是最长的。

class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
        #记录到下标i为止的最大连续子数组和
        dp = [0 for i in range(len(array))]
        dp[0] = array[0]
        maxsum = dp[0]
        #滑动区间
        left = 0
        right = 0
        #记录最长的区间
        resl = 0
        resr = 0 
        for i in range(1, len(array)):
            right += 1
            #状态转移：连续子数组和最大值
            dp[i] = max(dp[i - 1] + array[i], array[i]) 
            #区间新起点
            if dp[i - 1] + array[i] < array[i]:
                left = right
            #更新最大值
            if dp[i] > maxsum or dp[i] == maxsum and (right - left + 1) > (resr - resl + 1): 
                maxsum = dp[i]
                resl = left
                resr = right
        #取数组
        res = []
        for i in range(resl, resr + 1):
            res.append(array[i])
        return res
