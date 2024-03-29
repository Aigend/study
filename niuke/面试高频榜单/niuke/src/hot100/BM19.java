package hot100;

class BM19 {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型一维数组
     * @return int整型
     */
    public int findPeakElement (int[] nums) {
        // write code here
        int left = 0;
        int right = nums.length - 1;
        int n = nums.length;
        if (n==1) return 0;
        while (left < right){
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1]){
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    public static void main(String[] args) {

    }
}
