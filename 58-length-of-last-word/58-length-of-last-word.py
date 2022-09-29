class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n, result = len(s), 0
        words = s.split()
        last = words[-1]
        return len(last)
            