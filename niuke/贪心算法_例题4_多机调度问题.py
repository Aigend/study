"""
1、题目：n个作业组成的作业集，可由m台相同机器加工处理。要求给出一种作业调度方案，使所给的n个作业在尽可能短的时间内由m台机器加工处理完成。
2、思路：作业不能拆分成更小的子作业；每个作业均可在任何一台机器上加工处理。 这个问题是NP完全问题，还没有有效的解法(求最优解)，但是可以用贪心选择策略设计出较好的近似算法(求次优解)。当n<=m时，只要将作业时间区间分配给作业即可；当n>m时，首先将n个作业从大到小排序，然后依此顺序将作业分配给空闲的处理机。也就是说从剩下的作业中，选择需要处理时间最长的，把它分配给当前总累计需要工作时长最短的机器。这样一来，这个调度问题可以理解为一个分配问题，我们通过这种方案，使得几台机器获得接近的工作总时长，达到整体的最短的工作时长的效果。
	/**
	 * 贪心算法4：多机调度问题
	 */
	public void greedy4()
	{
		       int[] time= {9,7,8,4,2,1,3};
		       int number = 3;
		       
		       int Sumtime = getNumber4(time,number);
		
		       System.out.println("花费的最小总时间："+Sumtime);		
	}
	 /**
	 * 贪心算法4：多机调度问题
	 * @param time
	 * @param number
	 * @return
	 */
	public int getNumber4(int[] time, int number)
	{
		int usedTime=0;  //最长时间为总时间
		int[] fin = new int[number]; //单机处理时间		
		for(int k=0;k<number;k++) //初始时间清零
		{
			fin[k]=0;
		}		
		if(number>time.length)
			return time[0];
		else 
		{			
			for( int i=0 ; i<time.length-1 ;i++)
			{  
				   for( int j=0;j<time.length-i-1;j++) //冒泡选出任务时间最大的
				   {
					   if(time[j]>time[j+1])
					   {
						   int temp = time[j+1];
						   time[j+1]=time[j];
						   time[j]=temp;
					   }
				   }
					   int min=0;; 
					   int value=100;
					   for(int k=0;k<fin.length;k++)  //选出当前累计工时最小的机子
					   {
						   if(fin[k]<value)
						   {
							   min=k;
							   value=fin[k];
						   }						  
					   }					   						
					   fin[min]+=time[time.length-1-i];							   
			} 
			   int min=0;; 
			   int value=100;
			   for(int k=0;k<fin.length;k++)  //选出当前累计工时最小的机子
			   {
				   if(fin[k]<value)
				   {
					   min=k;
					   value=fin[k];
				   }				  
			   }
			   fin[min]+=time[0];
			for( int n=0;n<fin.length;n++)
			{
				if(fin[n]>usedTime)
				{
					usedTime=fin[n];
				}
			}
			return usedTime;
		}		
	}

"""