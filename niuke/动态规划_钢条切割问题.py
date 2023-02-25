"""
方法二 动态规划
此时，如果n=1，则不用切割，收益
R1 = 1，
n=2，可以选择切割成1 1，收益R = 1+1=2；也可以不切割 R=5，相比较不切割更优，R2=5。
n=3，切割成1 1 1，R=1+1+1=3；
或者切割成1 2，用上行中的R1 + R2 = 1+5=6，而不用再去讨论2是否要切割的问题，因为对于这种情况1 2两段，我们已经知道R2是怎么切割的了，所以这样就是最优的（已证）；
或者不切割 3，R=8 。
综上考虑
R3 = 8 是最优的。
n=4，切割方案有0+4，1+3，2+2，对应的收益分别是max（0+9，1+8，5+5（最优）），所以R4 =10=R2 +R2
n=5，有0+5，1+4，2+3，收益为max（0+10，1+10，5+8），所以R5=13
n=6，R6 = max（0+17，1+13，5+10，8+8）=17，所以R6=17
n=7，R7=max（0+17，1+17，5+13，8+10），R7=18
R8=22
R9=25
R10=30
···
总结：要想知道n长度钢条怎么切割最大，需要知道n-1钢条怎么切割最大，再去比较是1+（n-1）两段收益高还是不切割n直接卖收益高，依次比较max（n(如果n<10可以不切)，1+（n-1），2+（n-2），3+（n-3）…），然后后续要知道n-1最大收益，需要知道n-2怎么切割收益高，要知道···最后递归到n=1的时候的收益。

"""
#
#钢条切割问题：自顶向下（由大到小）
#
#获得最大值函数
def max(a,b):
    temp = a;
    if temp < b:
        temp = b;
    return temp

# 备忘机制的CUT-ROD
def MEMOIZED_CUT_ROD_AUX(p, n, r): # 实际上参数是输入的数字+1
    n = n - 1
    # 此时的n是输入的数
    if r[n] >= 0:
        return r[n]
    if n<=10:
        if n == 0:
            q = 0
        else:
            q = -9999
            for i in range(1, n):
                q = max(q, int(p[i]) + int(MEMOIZED_CUT_ROD_AUX(p, n - i, r)))
    
    else: 
    # 对于n>10的情况，同样要进行拆分成两个子问题再比较最大值，比如n=12应该还是得考虑max（1+11，2+10，3+9...）
        q = -9999
        for i in range(0, n):
            q = max(q, int(r[i+1]) + int(MEMOIZED_CUT_ROD_AUX(p, n - i, r)))
    r[n] = q
    print("n=",n)
    print("r=",r)
    return q

def MEMOIZED_CUT_ROD(p,n):
    r = {}
    for i in range(0,n):
        r[i] = -9999
    r[1] = p[0]
    return MEMOIZED_CUT_ROD_AUX(p,n,r)

if __name__ == '__main__':
    p = [1,5,8,9,10,17,17,20,24,30]
    #长度  i	 0   1	2	3	4	5	6	7	8	9	10
    #价格 pi     0 	 1	5	8	9	10	17	17	20	24	30
    print("输入钢条长度n：")
    n = int(input())
    if n == 1:
        print("最大的收益：",p[0])
    print("最大的收益：",MEMOIZED_CUT_ROD(p,n+1))

