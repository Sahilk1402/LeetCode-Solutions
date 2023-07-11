class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for n in nums:
            if n == 1:
                # Add 1 to curr when encounter 1
                curr += 1
                if curr > ans:
                    ans = curr
            else:
                # Add 1 to curr when encounter 1
                curr = 0
        return ans
