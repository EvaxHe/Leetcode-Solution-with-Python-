class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0,0 
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max ) # store previous max local_max for comparison
        return global_max