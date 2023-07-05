from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Method: Split the array in half at minimum price, and calculate maximum profit. Repeat until cannot split anymore.
        max_prof = 0
        min_price = 0
        max_price = 1
        # The array that will be split in half
        curr_prices = prices
        while curr_prices:
            min_price = min(curr_prices)
            max_price = max(curr_prices[curr_prices.index(min_price):])
            # Max prof for current minimum value calculated
            curr_prof = max_price - min_price
            if curr_prof > max_prof:
                max_prof = curr_prof
            curr_prices = curr_prices[:curr_prices.index(min_price)]
        return max_prof