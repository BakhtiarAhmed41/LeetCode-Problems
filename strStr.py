class Solution(object):
    def strStr(self, haystack, needle):
        
        if needle in haystack:
            for i in range(0, len(haystack)):
                if(i != len(haystack)-1):
                    if ((haystack[i] == needle[0]) and (haystack[i+1] == needle[1])):
                        return i
                    else:
                        continue
        else:
            return -1
