class Solution(object):
    def singleNumber(self, nums):
        
        nums.sort()
        if len(nums) == 1:
                    return nums[0]

        for i in range(len(nums)):
            if i == 0:
                if nums[0] != nums[1]:
                    return nums[0]
                continue

            elif i == len(nums)-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            
            elif nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]

        
