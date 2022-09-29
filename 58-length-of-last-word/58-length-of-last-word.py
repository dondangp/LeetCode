class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        last = word[-1]
        return len(last)
            