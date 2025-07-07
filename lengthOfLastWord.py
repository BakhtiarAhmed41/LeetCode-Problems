class Solution(object):
    def lengthOfLastWord(self, s):
        
        count = 0
        
        while (s.endswith(" ")):
            s = s[:-1]     

        for i in range(len(s)-1, -1, -1):
            
            if(s[i] != " " ):
                count = count+1
            
            else:
                break

        return count
        
