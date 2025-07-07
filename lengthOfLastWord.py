class Solution(object):
    def lengthOfLastWord(self, s):
        
        count = 0

        for i in range(len(s)-1, 0, -1):
            
            if(s[i] == " "):
                continue
            
            elif(s[i] != " " ):
                count = count+1
            
            else:
                break

        return count
        
