import java.util.*;


class TwoSum {

    /**
     * NC61 两数之和
     * @param numbers int整型一维数组 
     * @param target int整型 
     * @return int整型一维数组
     */
    public int[] twoSum (int[] numbers, int target) {
        // write code here
//        HashSet<Integer> hashSet = new HashSet<>();
//        for(int i:numbers){
//            int tmp = target - i;
//            if(hashSet.contains(tmp)){
//                return new int[]{tmp, i};
//            }
//            hashSet.add(i);
//        }
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for(int i=0; i<numbers.length; i++){
            int tmp = target - numbers[i];
            if(hashMap.get(tmp) != null){
                return new int[]{hashMap.get(tmp)+1, i+1};
            }
            hashMap.put(numbers[i], i);
        }
        return new int[2];
    }

    public static void main(String[] args) {
        int[] res = new TwoSum().twoSum(new int[]{1,3,4,6,7,8}, 11);
        System.out.println(Arrays.toString(res));
    }
}