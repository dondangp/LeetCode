class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        
        for i in range(len(words)):
            if words[i] not in sentence:
                return False
        return True
            