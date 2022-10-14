class Solution:
    def climbStairs(self, n: int) -> int:
        #set two variables
        one,two = 1,1
        #iterating through n-1
        for i in range (n-1):
            #making new variable
            temp = one
            one = one + two
            two = temp
        return one