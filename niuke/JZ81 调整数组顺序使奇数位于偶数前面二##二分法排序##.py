描述
输入一个长度为 n 整数数组，数组里面可能含有相同的元素，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，
对奇数和奇数，偶数和偶数之间的相对位置不做要求，但是时间复杂度和空间复杂度必须如下要求。

class Solution:
    def reOrderArrayTwo(self , array: List[int]) -> List[int]:
        # write code here
        left = 0
        right = len(array) -1
        while left < right:
            while left < right and array[left] % 2:
                left += 1
            while right > left and array[right]% 2==0:
                right -= 1
            array[left], array[right] = array[right], array[left]
        return array