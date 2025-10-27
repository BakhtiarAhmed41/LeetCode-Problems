class Solution(object):
    def containsDuplicate(self, nums):
        
        for i in range(len(nums)):

            if count(nums[i]) > 1:
                return True
            continue
        return False


        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
            
        # return False
        
