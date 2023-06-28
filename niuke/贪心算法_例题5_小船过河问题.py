"""
N个人过河，船每次只能坐两个人，船载每个人过河的所需时间不同t[i]，
每次过河的时间为船上的人的较慢的那个，求最快的过河时间。(船划过去要有一个人划回来)
2、思路：本题的最优选择是先将所有人过河所需的时间按照升序排序。优先把速度慢的人带到对岸，返回由速度快的人来完成，
节省时间，在剩余人数大于3时，有两种方式：

 1.最快的和次快的过河，然后最快的将船划回来；次慢的和最慢的过河，
然后次快的将船划回来，所需时间为：t[0]+2t[1]+t[n-1]；

2.最快的和最慢的过河，然后最快的将船划回来，最快的和次慢的过河
，然后最快的将船划回来，所需时间为：2t[0]+t[n-2]+t[n-1]。最后还需处理一下人数小于等于3的边界问题。


	/**
	 * 贪心算法5：小船过河问题
	 */
	public void greedy5()
	{
		       int[] v = {1,3,4,8,4,3,9}; //按照不同的人的速度过河所需的时间
		       int timeSum=getNumber5(v);
		       System.out.println("过河总时间："+timeSum);
	}
          /** 
	 * 贪心算法5：小船过河问题
	 */
	public int getNumber5(int[] v)
	{
		int time =0;;
		Arrays.sort(v);//降序排列
		int N = v.length; //N表示当前人数
		while(N>3)
		{
			if(2*v[0]+v[N-1]+v[N-2]>2*v[1]+v[0]+v[N-1])
				time+=2*v[1]+v[0]+v[N-1];
			else
				time+=2*v[0]+v[N-1]+v[N-2];
			N-=2;
		}
		else if(N==3) //处理边界
		{
			time+=v[2]+v[0]+v[1];
		}
		else if(N==2)
		{
			time+=v[1];
		}
		else if(N==1)
		{
			time+=v[0];
		}	
		return time;		
	}

"""