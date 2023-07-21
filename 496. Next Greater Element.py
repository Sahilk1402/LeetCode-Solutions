class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        return [d.get(no,-1)for no in nums1]
