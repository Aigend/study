描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符 "go" 时，第一个只出现一次的字符是 "g" 。
当从该字符流中读出前六个字符 “google" 时，第一个只出现一次的字符是"l"。
后台会用以下方式调用 Insert 和 FirstAppearingOnce 函数

string caseout = "";
1.读入测试用例字符串casein
2.如果对应语言有Init()函数的话，执行Init() 函数
3.循环遍历字符串里的每一个字符ch {
Insert(ch);
caseout += FirstAppearingOnce()
}
2. 输出caseout，进行比较。

class Solution:
    def __init__(self):
        self.s = ""
        self.mp = dict()
        
    def FirstAppearingOnce(self):
        #遍历字符串
        for c in self.s:
            #找到第一个出现次数为1的
            if self.mp[c] == 1:
                return c
        #没有找到
        return '#' 
        
    def Insert(self, char):
        #插入字符
        self.s += char  
        #哈希表记录字符出现次数
        if char in self.mp:
            self.mp[char] += 1
        else:
            self.mp[char] = 1
