class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit =0

        left= 0
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left =right
                right+=1
            else:
                current_profit = max(current_profit, prices[right]-prices[left])
                right+=1
        
        return current_profit