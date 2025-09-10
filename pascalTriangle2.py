import math

class Solution(object):
    def getRow(self, rowIndex):
        row = []
        for k in range(rowIndex + 1):
            value = int(math.factorial(rowIndex) / (math.factorial(k) * math.factorial(rowIndex - k)))
            row.append(value)
        return row
