from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = 0
        max_price = 1
        curr_prices = prices
        while curr_prices:
            min_price = min(curr_prices)
            max_price = max(curr_prices[curr_prices.index(min_price):])
            curr_prof = max_price - min_price
            if curr_prof > max_prof:
                max_prof = curr_prof
            curr_prices = curr_prices[:curr_prices.index(min_price)]
        return max_prof