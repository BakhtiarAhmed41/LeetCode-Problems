class Solution(object):
    def totalMoney(self, n):
        add = 0
        sum = 0
        for i in range(n):

            if (i%7==0):
                add = (i / 7) +1
                sum = sum + add
            
            else:    
                add = add+1
                sum = sum + add

        return sum
        

