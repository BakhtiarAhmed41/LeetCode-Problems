class Solution(object):
    def majorityElement(self, nums):
        
        return max(nums, key=nums.count)
        
