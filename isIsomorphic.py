class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False
        
        mapST = {}  # mapping from s → t
        mapTS = {}  # mapping from t → s
        
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            
            # If mapping exists, check consistency
            if ch1 in mapST:
                if mapST[ch1] != ch2:
                    return False
            else:
                mapST[ch1] = ch2
            
            # Also check reverse mapping
            if ch2 in mapTS:
                if mapTS[ch2] != ch1:
                    return False
            else:
                mapTS[ch2] = ch1
        
        return True
