"""
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。
"""
s = input()
res = []
tmp = set()
for k in reversed(s):
    if k not in tmp:
        res.append(k)
        tmp.add(k)
print(int("".join(res)))
