"""
给定两个字符串str1和str2，返回两个字符串的最长公共子序列，
例如：str1="1A2C3D4B56",str2="B1D23CA45B6A","123456"和"12C4B6"都是最长公共子序列，返回哪一个都行。

分析：本题是非常经典的动态规划问题，假设str1的长度为M，str2的长度为N，则生成M*N的二维数组dp，
dp[i][j]的含义是str1[0..i]与str2[0..j]的最长公共子序列的长度。

dp值的求法如下：
dp[i][j]的值必然和dp[i-1][j],dp[i][j-1],dp[i-1][j-1]相关，
结合下面的代码来看，
我们实际上是从第1行和第1列开始计算的，而把第0行和第0列都初始化为0，
这是为了后面的取最大值在代码实现上的方便，dp[i][j]取三者之间的最大值。


#include <iostream>
#include <string>
#include <stack>
using namespace std;
void LCS(string s1,string s2)
{
    int m=s1.length()+1;
    int n=s2.length()+1;
    int **c;
    int **b;
    c=new int* [m];
    b=new int* [m];
    for(int i=0;i<m;i++)
    {
        c[i]=new int [n];
        b[i]=new int [n];
        for(int j=0;j<n;j++)
            b[i][j]=0;
    }
    for(int i=0;i<m;i++)
        c[i][0]=0;
    for(int i=0;i<n;i++)
        c[0][i]=0;
    for(int i=0;i<m-1;i++)
    {
        for(int j=0;j<n-1;j++)
        {
            if(s1[i]==s2[j])
            {
                c[i+1][j+1]=c[i][j]+1;
                b[i+1][j+1]=1;          //1表示箭头为  左上
            }
            else if(c[i][j+1]>=c[i+1][j])
            {
                c[i+1][j+1]=c[i][j+1];
                b[i+1][j+1]=2;          //2表示箭头向  上
            }
            else
            {
                c[i+1][j+1]=c[i+1][j];
                b[i+1][j+1]=3;          //3表示箭头向  左
            }
        }
    }
    for(int i=0;i<m;i++)                //输出c数组
    {
        for(int j=0;j<n;j++)
        {
            cout<<c[i][j]<<' ';
        }
        cout<<endl;
    }
    stack<char> same;                   //存LCS字符
    stack<int> same1,same2;             //存LCS字符在字符串1和字符串2中对应的下标，方便显示出来
    for(int i = m-1,j = n-1;i >= 0 && j >= 0; )
    {
        if(b[i][j] == 1)
        {
            i--;
            j--;
            same.push(s1[i]);
            same1.push(i);
            same2.push(j);
        }
        else if(b[i][j] == 2)
                i--;
             else
                j--;
    }
    cout<<s1<<endl;                     //输出字符串1
    for(int i=0;i<m && !same1.empty();i++)      //输出字符串1的标记
    {
        if(i==same1.top())
        {
            cout<<1;
            same1.pop();
        }
        else
            cout<<' ';
    }
    cout<<endl<<s2<<endl;                //输出字符串2
    for(int i=0;i<n && !same2.empty();i++)      //输出字符串2的标记
    {
        if(i==same2.top())
        {
            cout<<1;
            same2.pop();
        }
        else
            cout<<' ';
    }
    cout<<endl<<"最长公共子序列为：";
    while(!same.empty())
    {
        cout<<same.top();
        same.pop();
    }
    cout<<endl<<"长度为："<<c[m-1][n-1]<<endl;
    for (int i = 0; i<m; i++)
    {
        delete [] c[i];
        delete [] b[i];
    }
    delete []c;
    delete []b;
}
int main()
{
    string s1="ABCPDSFJGODIHJOFDIUSHGD";
    string s2="OSDIHGKODGHBLKSJBHKAGHI";
    LCS(s1,s2);
    return 0;
}
"""

# https://blog.csdn.net/weixin_40673608/article/details/84262695/

class Soultion:

    def LCS(str1:str, str2:str):
        