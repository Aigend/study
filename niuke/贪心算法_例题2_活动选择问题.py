"""
 有n个需要在同一天使用同一个教室的活动a1,a2,…,an，教室同一时刻只能由一个活动使用。
 每个活动ai都有一个开始时间si和结束时间fi ，一旦被选择后，活动ai就占据半开时间区间[si,fi)。
 如果[si,fi]和[sj,fj]互不重叠，ai和aj两个活动就可以被安排在这一天，
 该问题就是要安排这些活动使得尽量多的活动能不冲突的举行。
 例如下图所示的活动集合S，其中各项活动按照结束时间单调递增排序。
	/**
	 * 贪心算法2：活动选择问题
	 */
	public void greedy2(){		  
			   int [] st = {1,5,0,5,3,3,6,8,8,2,12};
			   int [] et = {4,9,6,7,8,5,10,12,11,13,14};			
			   int num = getNumber2(st,et);
			   System.out.println("活动数量："+num);		
	}
	/**
	 * 贪心算法2：活动选择问题
	 * @param a
	 * @param b
	 * @return
	 */
	public int getNumber2(int[] a , int[] b)  //优先选择结束时间早的
	{
		int num=0;
		int tempa=0;
		int tempb=0;
		int endTime=0;
		int j=0;
		for(int i=1;i<b.length;i++)//如果顺序混乱，则调整为结束时间从小到大的顺序,直接插入排序
		{
			    tempb=b[i];
				tempa=a[i];
			for(j=i-1;j>=0&&tempb<b[j];j--)
			{								
					b[j+1]=b[j];
					a[j+1]=a[j];
					if(j==0)
					{
						j--;
						break;
					}
			}
			    b[j+1]=tempb;
				a[j+1]=tempa;				
		}
		System.out.println(Arrays.toString(a));
		System.out.println(Arrays.toString(b));		
		num++;
		endTime=b[0];
		for(int k=1;k<b.length;k++)
		{
			if(a[k]>endTime)
			{
				num++;
				endTime=b[k];				
			}
		}						
		return num;								
	   }	
     }

"""
