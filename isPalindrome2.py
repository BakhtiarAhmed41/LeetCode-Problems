class Solution(object):
    def isPalindrome(self, s):
        filtered = ""
        for ch in s:
            if ch.isalnum():  
                filtered += ch.lower()

        i = 0
        while i < len(filtered) - i - 1:
            if filtered[i] != filtered[len(filtered) - i - 1]:
                return False
            i += 1
        return True
