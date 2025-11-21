class Solution(object):
    def missingNumber(self, nums):
        
        for i in range(0,len(nums)+1):
            sorted(nums)

            if i == len(nums):
                return i

            elif i != nums[i]:
                return i
        
