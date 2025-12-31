class Solution(object):
    def findRelativeRanks(self, score):
        rank = []    
        sort = sorted(score, reverse=True)

        for i in range(len(score)):
            
            if sort.index(score[i])+1 == 1:
                rank.append("Gold Medal")
            
            elif sort.index(score[i])+1 == 2:
                rank.append("Silver Medal")

            elif sort.index(score[i])+1 == 3:
                rank.append("Bronze Medal")
            
            else:
                rank.append(str(sort.index(score[i]) + 1))
        return rank
        
