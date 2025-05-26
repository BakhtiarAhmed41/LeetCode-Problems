class Solution(object):
    def twoSum(self, nums, target):
        indices = []

        for i in range(len(nums)):

            for j in range(len(nums)):
                if (j==i):
                    continue
                
                elif(nums[i] + nums[j] == target):
                        indices.append(i)
                        break
                
                else:
                    continue
        
        return indices
        
