class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        newString = s.split()
     #   newK = k - 1
        returnString = ""
        
        for i in range(k):
            if i == 0:
                returnString += newString[i]
            else:
                returnString += " " + newString[i]
        
        return returnString
    #return newString[newK]
        
        
                
        