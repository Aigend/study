"""
描述
给定一个数组 nums 和一个正整数 target , 找出满足和大于等于 target 的长度最短的连续子数组并返回其长度，如果不存在这种子数组则返回 0。

数据范围：数组长度满足 1 \le n \le 10^5 \1≤n≤10 
5
   ，数组中的元素满足 1 \le val \le 10^5 \1≤val≤10 
5
   ， 1 \le target \le 10^5 \1≤target≤10 
5
"""
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def minSubarray(self , nums: List[int], target: int) -> int:
        # write code here
        #左右指针移动滑窗求长度
        left = 0          #左指针
        right = 0         #右指针
        sums = 0          #左右指针滑窗内部的值之和
        ans = len(nums)   #这个是用来比较滑窗内长短的值，可以设为无限大，这里我设为nums长度
        while right < len(nums):     #右指针先走，走完整个nums
            while right < len(nums) and sums < target:   
            #这里再次限定了右指针行动范围，同时讨论sums没有大于target的情况
            #这种时候就要把右指针右移，扩大标定范围，同时将sums加上右移添加的值
                sums += nums[right]
                right += 1
            while left <right and sums >= target:
            #这里则是使得保证左指针小于右指针，且当sums是大于等于target时的情况
            #这种情况是满足要求的，但是需要比较所含范围的长短
                ans  = min(ans,right-left) #比较长短，最后就已经可以得到ans
                sums -= nums[left] #如果长了就右移左指针，减去值
                left += 1
        return ans
