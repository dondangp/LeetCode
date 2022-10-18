class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #26 letters in alphabet
        if len(set(sentence)) == 26:
            #return true
            return 1 
        #return false
        else:
            return 0
        
            