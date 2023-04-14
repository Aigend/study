##面试kmp##_求next数组

"""
https://blog.csdn.net/yearn520/article/details/6729426
看懂原理算法实现就比较简单了
上面的理论我们就能得到下面的前缀next数组的求解算法。
void SetPrefix(const char *Pattern, int prefix[])
{
     int len=CharLen(Pattern);//模式字符串长度。
     prefix[0]=0;
     for(int i=1; i<len; i++)
     {
         int k=prefix[i-1];
         //不断递归判断是否存在子对称，k=0说明不再有子对称，Pattern[i] != Pattern[k]说明虽然对称，但是对称后面的值和当前的字符值不相等，所以继续递推
         while( Pattern[i] != Pattern[k]  &&  k!=0 )               
             k=prefix[k-1];     //继续递归
         if( Pattern[i] == Pattern[k])//找到了这个子对称，或者是直接继承了前面的对称性，这两种都在前面的基础上++
              prefix[i]=k+1;
         else
              prefix[i]=0;       //如果遍历了所有子对称都无效，说明这个新字符不具有对称性，清0
     }

}
"""
def set_prefix(pattern:str, next=[]):
  next[0]=0
  for i in range(1, len(pattern)):
    k = next[i-1]
    while pattern[i]!=pattern[k]:
      k = next[k-1] # 持续递归  
      if k == 0:
        break
   if pattern[i] == pattern[k]:
      next[i] = k+1
   else:
      next[i] = 0
