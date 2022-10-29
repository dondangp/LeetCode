class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, sell, min, ans = 0,1,0,0
        while sell < len(prices):
            if prices[buy] > prices[min]:
                buy = min
            ans = max(ans,prices[sell]-prices[buy])
            if prices[sell] < prices[min]:
                min = sell
            sell +=1
        return ans