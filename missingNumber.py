class Solution(object):
    def missingNumber(self, nums):
        
        for i in range(0,len(nums)+1):
            nums = sorted(nums)

            if i == len(nums):
                return i

            else:
                if i != nums[i]:
                    return i
        
