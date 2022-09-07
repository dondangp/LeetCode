class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int step_one=0;
        int step_two=0;

        for(int i = cost.length-1;i>=0;i--)
        {
            int alg = cost[i] + Math.min(step_one,step_two);
                step_one = step_two;
                step_two = alg;
                
        }
        
        return Math.min(step_one,step_two);
        
        
        
        
        
    }
}