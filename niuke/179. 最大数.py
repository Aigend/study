给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

方法一：选择排序
思路
两个数字对应的字符串a和b，如果字典序a+b>b+a，此时a排在b的前面即可获得更大值
示例：a=3,b=32,两者拼接的值：332>323，所以3应排在32前面

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=len(nums)
        nums=list(map(str,nums))
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        
        return str(int("".join(nums)))

作者：yim-6
链接：https://leetcode.cn/problems/largest-number/solution/python3-san-chong-fang-fa-qiu-zui-da-shu-cpi4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
