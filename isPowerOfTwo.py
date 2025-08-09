class Solution(object):
    def isPowerOfTwo(self, n):
        
        if n <= 0:
            return False

        elif(n>1):
            while(n != 1):    
                if n % 2 != 0:  
                    return False
                n //= 2 
        
        return True
