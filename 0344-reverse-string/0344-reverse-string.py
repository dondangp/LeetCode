class Solution:
    def reverseString(self, s: List[str]) -> None:
        sLen = len(s)
        for i in range(sLen//2):
            #swap is awesome in python
            s[i], s[sLen-1-i] = s[sLen-1-i], s[i]