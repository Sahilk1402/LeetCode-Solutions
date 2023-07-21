class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set([])

        def dfs(nums,path,res,visited):
            if len(path) == len(nums):
                res.append(path+[])
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(nums,path,res,visited)
                    path.pop()
                    visited.discard(i)
        dfs(nums,[],res,visited)
        return res
