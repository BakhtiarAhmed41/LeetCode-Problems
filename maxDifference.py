class Solution(object):
    def maxDifference(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        odds = []
        evens = []

        for count in freq.values():
            if count % 2 == 0:
                evens.append(count)
            else:
                odds.append(count)
        
        if not odds or not evens:
            return -1
        
        max_diff = float('-inf')
        for o in odds:
            for e in evens:
                max_diff = max(max_diff, o - e)
        
        return max_diff
