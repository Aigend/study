283_移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     while left < right and nums[left]!=0:
        #         left += 1
        #     while left < right and nums[right]==0:
        #         right -= 1
        #     if left < right:
        #         nums[left], nums[right]=nums[right], nums[left]
        # return nums
        ret = 0
        j = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                ret+=1
                nums[j]=nums[i]
                j+=1
        for i in range(ret, len(nums)):
            nums[i]=0
        return nums
