1004_最大连续1的个数III

给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
class Solution {
public:
    int longestOnes(vector<int> &nums, int k) {
        // 起始指针、0的个数
        int i = 0, cnt = 0, len = nums.size(), res = 0;
        // 不断后移终止指针
        for (int j = 0; j < len; ++j) {
            // 更新0的个数
            if (nums[j] == 0)cnt++;
            // 在不满足cnt≤k的情况下，保守地将起始指针后移，一旦满足cnt≤k，立即停止移动
            while (cnt > k) {
                // 更新0的个数，起始指针后移
                if (nums[i++] == 0)cnt--;
            }
            // 一旦满足条件就更新结果
            res = max(res, j - i + 1);
        }
        return res;
    }
}
