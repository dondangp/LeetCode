class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        last = a[-1]
        return len(last)