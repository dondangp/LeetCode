class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(set(sentence)) == 26:
            return 1
        else:
            return 0