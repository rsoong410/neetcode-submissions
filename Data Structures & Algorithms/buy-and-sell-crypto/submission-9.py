class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1

        if not prices or len(prices)==1:
            return 0
        
        profit = max(0, prices[right]-prices[left])

        while right<len(prices):

            profit =max(profit, prices[right]-prices[left])

            if prices[right] <= prices[left]:
                left=right
                right+=1
                
            elif prices[right]>prices[left]:
                right+=1
                
        return profit 
