"""
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）"""
import sys
s = input()
c = input()
result = 0
for k in s:
    if k.lower()==c.lower():
        result+=1
print(result)
