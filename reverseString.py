class Solution(object):
    def reverseString(self, s):
        x = ""
        for i in s:
            x += i

        for i in range(len(s)):
            s[i] = x[len(x)-i-1]

        return s
