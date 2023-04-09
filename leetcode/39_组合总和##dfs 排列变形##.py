39_组合总和##dfs 排列变形##

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。
你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。


输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

# 本题需要注意，无重复数字，同一个数字可以无限制获取
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []
#         path = []
#         if len(
#         dfs(candidates, target, result, ret)
#         return result

#       def dfs(candidates, target, result, ret)
#           if sum(ret)==target:
#               result.append(copy.copy(ret))
#               return
#           for v in candidates:
#               if v in 

# 要避免重复元素
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        if not len(candidates):
            return result
        path = []

        def dfs(candidates, target, result, path, index, size):
            if sum(path)==target:
                result.append(path)
                return
            elif sum(path) > target:
                return
            for i in range(index, size): # 为什么设置index 看这里https://leetcode.cn/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
                dfs(candidates, target, result, path+[candidates[i]], i, size)
        index = 0 
        size = len(candidates)
        dfs(candidates, target, result, path, index, size)
        return result
