

//滑动窗口
int minSubArrayLen(int target, int* nums, int numsSize){
    int left=0,right=0;//起始和终止位置指针
    int sum=0;//窗口元素和
    int min=numsSize+1;//满足条件的最短窗口长度 因为有可能刚好整个数组和等于或大于target，所以size+1
    int len=0;//窗口长度

    while(right<numsSize)
    {
        sum=sum+nums[right];
        while(sum>=target)//用while是为了收缩窗口  1 1 1 1 100   target=100
        {
            len=right-left+1;//窗口长度
            min=min<len?min:len;
            sum=sum-nums[left];
            left++;
        }
        right++;
    }
    return min==numsSize+1?0:min;
    //如果min还是等于numsSize+1，则 整个数组元素和 < target,出0；
    //如果不等于，则min=numsSize或者是正常情况
}

作者：qi-yue-xu9
链接：https://leetcode.cn/problems/minimum-size-subarray-sum/solution/209-chang-du-zui-xiao-de-zi-shu-zu-by-qi-epfp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
