
1-a
2-b
3-c
...
26-z
27-aa
28-ab


# 差点未接出来
num = int(input())
s = ""
while num:
    num -= 1
    tmp = chr(ord("a") + num % 26)
    num //= 26
    s += tmp

print(s.strip()[::-1])
