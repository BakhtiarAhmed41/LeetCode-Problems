class Solution(object):
    def moveZeroes(self, nums):
        
        nums2 = []
        nums2 = nums

        nums2.sort()
        nums.remove(0)

        for i in nums2:
            if i == 0:
                nums.append(i)


        return nums

    
