class Solution(object):
    def plusOne(self, digits):
        
        # dig = ""

        # for i in digits:
        #     dig[i] = digits[i]

        dig = ' '.join(map(str,digits))
        dig = dig.replace(" ", "")
        dig = int(dig)
        dig = str(dig + 1)
        

        result =[]
        for i in range(len(dig)):
            result.append(int(dig[i]))
        
        return result
