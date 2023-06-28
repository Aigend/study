"""
明明生成了
�
N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
"""
# import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
n = int(input())
tmp = set()
res = []
for i in range(n):
    k = int(input())
    if k not in tmp:
        tmp.add(k)
        res.append(k)
m = len(res)
for i in range(m):
    for j in range(m-1-i):
        if res[j]>res[j+1]:
            res[j+1],res[j]=res[j], res[j+1]
for i in range(m):
    print(res[i])
