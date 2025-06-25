class Solution(object):
    def isValid(self, s):
        
        result = True

        if "(" in s:
            if ")" in s and s.count("(") == s.count(")"):
                result = True
            else:
                result = False
        
        if "[" in s:
            if "]" in s and s.count("[") == s.count("]"):
                result = True
            else:
                result = False
        
        if "{" in s:
            if "}" in s and s.count("{") == s.count("}"):
                result = True
            else:
                result = False

    
        return result
        
