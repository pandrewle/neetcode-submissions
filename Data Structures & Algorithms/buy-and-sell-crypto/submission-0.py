class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lower = prices[0]

        for price in prices:
            if price < lower:
                lower = price
            res = max(res, price-lower)
        return res