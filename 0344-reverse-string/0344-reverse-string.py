class Solution:
    def reverseString(self, s: List[str]) -> None:
        wholeLength = len(s)
        for i in range(wholeLength//2):
            #swap
            s[i], s[wholeLength-1-i] = s[wholeLength-1-i], s[i]
