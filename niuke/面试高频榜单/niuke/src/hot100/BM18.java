package hot100;

class BM18 {
    public boolean Find(int target, int[][] array) {
        int m = array.length;
        int n = array[0].length;
        for (int i = m-1, j = 0; i >= 0 && j < n; ) {
            if (array[i][j] > target){
                i--;
            } else if (array[i][j]<target) {
                j++;
            } else {
                return true;
            }
        }
        return false;
    }
}
