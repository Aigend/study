package hot100;

import java.util.*;


class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型一维数组
     * @param target int整型
     * @return int整型
     */
    public int search (int[] nums, int target) {
        // write code here
        int left=0;
        int right=nums.length-1;
        while(left<=right){
            // int mid = left + (right-left)/2;
            int mid = (left + right)/2;
            System.out.println("mid:" + mid + "--->" + nums[mid] + "--->" + target);
            if(nums[mid]>target){
                right = mid -1;
            }else if(nums[mid]<target){
                left = mid + 1;
            }else{
                return mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[] {-1, 1};
        int target = -1;
        System.out.println(solution.search(nums, target));
    }
}
