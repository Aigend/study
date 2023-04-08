描述
用x,y表示一个整数范围区间，现在输入一组这样的范围区间(用空格隔开)，请输出这些区间的合并。
输入描述：
一行整数，多个区间用空格隔开。区间的逗号是英文字符。
输出描述：
合并后的区间，用过空格隔开，行末无空格
nums = []
a = input()


for num in a.split():
    tmp = []
    for v in num.split(","):
        tmp.append(int(v))
    nums.append(tmp)



def sort_l(elem):
    return elem[0]


nums.sort(key=sort_l)

res = []
tmp = nums[0]
for i in range(1, len(nums)):
    if tmp[1] >= nums[i][0]:
        tmp = [tmp[0], max(tmp[1], nums[i][1])]
    else:
        res.append(tmp)
        tmp = nums[i]
res.append(tmp)
print(" ".join([",".join([str(x) for x in r]) for r in res]))
