"""
实现整数数组从大到小降序排序，要求：不使用语言自带排序能力
如：[1,4,3,5]降序排序后是[5,4,3,1]
"""
nums = input()
nums = [int(num) for num in nums.split(",")]
# print(nums)
n = len(nums)
for i in range(n):
    # flag = False
    for j in range(1, n-i):
        if nums[j] > nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
    #         flag = True
    # if not flag:
    #     break
print(nums)