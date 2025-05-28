class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        arr = []

        if(len(num)==1):
            return True
        else:
            for i in range(len(num)):
                arr.append(num[i])
            
            for i in range(len(arr)/2):

                
                if(i == len(arr)/2 - 1):
                    if(arr[i] == arr[len(arr)-i-1]):
                        return True
                    else:
                        return False

                elif(arr[i] == arr[len(arr)-i-1]):
                    continue

                else:
                    return False    
            
