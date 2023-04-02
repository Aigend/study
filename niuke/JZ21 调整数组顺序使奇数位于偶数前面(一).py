"""
描述
输入一个长度为 n 整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
a = input()
l = eval(a)
if not l:
    print(l)
    print("***")
else:
    left = 0
    right = len(l)-1
    while left < right:
        while left < right and l[left] % 2!=0:
            left += 1
        while left < right and l[right] % 2==0:
            right -= 1
        if left <= right:
            l[left], l[right] = l[right], l[left]
    print(l)
    
    # 未调通，感觉是ACM刷题模式下返回的格式不对
