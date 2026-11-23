class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Window
        # Start -> the day to buy
        # End -> the day to sell

        n = len(prices)

        # Max profit is 0 because we would choose not to buy if there was only one day.
        if n == 1:
            return 0

        i_buy = 0  # The day we choose to buy
        i_sell = 1 # The day we choose to sell

        max_profit = 0
        min_buy = prices[0]

        # profit = sell_price - buy_price
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])

        return max_profit