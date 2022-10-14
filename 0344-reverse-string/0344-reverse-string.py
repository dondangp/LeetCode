class Solution:
    def reverseString(self, s: List[str]) -> None:
        wholelength = len(s)
        for i in range(wholelength//2):
            s[i],s[wholelength-1-i] = s[wholelength-1-i], s[i]
            
