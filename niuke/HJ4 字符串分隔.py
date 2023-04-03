"""
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串
"""
# s= input()
# while len(s) >0:
#     temp = s[:8]
#     if len(temp)<8:
#         temp+="0"*(8-len(temp))
#         print(temp)
#         break
#     print(temp)
#     s=s[8:]

s = input()
while len(s) > 8:
    print(s[:8])
    s = s[8:]
if len(s)>0:
    print(s.ljust(8, "0"))
