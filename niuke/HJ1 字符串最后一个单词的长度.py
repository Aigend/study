"""
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
"""
import sys

for line in sys.stdin:
    a = line.split()
    print(len(a[-1]))
