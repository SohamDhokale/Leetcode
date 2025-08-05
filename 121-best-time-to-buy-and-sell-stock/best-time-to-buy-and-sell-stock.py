class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Initialize the minimum price to infinity
        min_price = float('inf')
      
        # Loop through the prices
        for price in prices:
            # Update the maximum profit if the current price minus the minimum price seen so far is greater
            max_profit = max(max_profit, price - min_price)
            # Update the minimum price seen so far if the current price is lower
            min_price = min(min_price, price)
          
        # Return the maximum profit achieved
        return max_profit