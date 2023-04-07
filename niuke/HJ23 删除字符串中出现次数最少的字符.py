描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
s = input()
tmp = {}
l = []
for k in s:
    tmp[k]=tmp.get(k, 0) + 1
t = min(tmp.values())
for k in s:
    if tmp[k] != t:
        l.append(k)
print("".join(l))
