# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : NC7 买卖股票的最好时机(一).py
# @Date    : 2022/09/08:21:41
# @Author  : jinwenlong@oppo.com
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        #维护最大收益
        res = 0 
        #排除特殊情况
        if len(prices) == 0: 
            return res
        #维护最低股票价格
        Min = prices[0] 
        #遍历后续股票价格
        for i in range(1, len(prices)): 
            #维护最大值
            res = max(res, prices[i] - Min) 
            #如果当日价格更低则更新最低价格
            Min = min(Min, prices[i]) 
        return res
