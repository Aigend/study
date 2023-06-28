BM54 三数之和

思路：
直接找三个数字之和为某个数，太麻烦了，我们是不是可以拆分一下：如果找到了某个数a，要找到与之对应的另外两个数，三数之和为0，那岂不是只要找到另外两个数之和为−a？这就方便很多了。
因为三元组内部必须是有序的，因此可以优先对原数组排序，这样每次取到一个最小的数为a，只需要在后续数组中找到两个之和为−a就可以了，我们可以用双指针缩小区间，因为太后面的数字太大了，就不可能为
−a，可以舍弃。

具体做法：

step 1：排除边界特殊情况。
step 2：既然三元组内部要求非降序排列，那我们先得把这个无序的数组搞有序了，使用sort函数优先对其排序。
step 3：得到有序数组后，遍历该数组，对于每个遍历到的元素假设它是三元组中最小的一个，那么另外两个一定在后面。
step 4：需要三个数相加为0，则另外两个数相加应该为上述第一个数的相反数，我们可以利用双指针在剩余的子数组中找有没有这样的数对。双指针指向剩余子数组的首尾，如果二者相加为目标值，那么可以记录，而且二者中间的数字相加可能还会有。
step 5：如果二者相加大于目标值，说明右指针太大了，那就将其左移缩小，相反如果二者相加小于目标值，说明左指针太小了，将其右移扩大，直到两指针相遇，剩余子数组找完了。
注：对于三个数字都要判断是否相邻有重复的情况，要去重。

class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        res = list(list())
        n = len(num)
        #不够三元组
        if n < 3: 
            return res
        #排序
        num.sort() 
        for i in range(n - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue
            #后续的收尾双指针
            left = i + 1 
            right = n - 1
            #设置当前数的负值为目标
            target = -num[i] 
            while left < right:
                #双指针指向的二值相加为目标，则可以与num[i]组成0
                if num[left] + num[right] == target: 
                    res.append([num[i], num[left], num[right]])
                    while left + 1 < right and num[left] == num[left + 1]:
                        #去重
                        left += 1 
                    while right - 1 > left and num[right] == num[right - 1]:
                        #去重
                        right -= 1 
                    #双指针向中间收缩
                   left += 1 
                    right -= 1
                #双指针指向的二值相加大于目标，右指针向左
                elif num[left] + num[right] > target: 
                    right -= 1
                #双指针指向的二值相加小于目标，左指针向右
                else: 
                    left += 1 
        return res
