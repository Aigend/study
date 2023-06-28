描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

import sys
n = int(input())
s = {}
for line in sys.stdin:
    a = line.split()
    s[int(a[0])] = s.get(int(a[0]), 0) + int(a[1])
# for k, v in s.items():
#     print(k, v)
# 输出按照index值升序进行输出。
key = sorted(s.keys())
for k in key:
    print(k, s[k])
