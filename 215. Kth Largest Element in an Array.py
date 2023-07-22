# Direct
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums,reverse =True)
        return res[k-1]

# Using Heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build Min Heap
        heapq.heapify(nums)
        #remove n-k smallest number
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        
