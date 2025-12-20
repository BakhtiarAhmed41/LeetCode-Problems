class Solution(object):
    def titleToNumber(self, columnTitle):
        x = [
            'A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z'
        ]

        y = 0
        for char in columnTitle:
            y = y * 26 + (x.index(char) + 1)

        return y
