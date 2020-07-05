'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: list) -> int:
        if prices:
            # dynamic programming
            first_buy, first_profit, second_buy, final_profit = float('inf'), 0, float('inf'), 0
            for curPrice in prices:
                first_buy = min(first_buy, curPrice)  # keep minimal
                first_profit = max(first_profit, curPrice - first_buy)  # maximum if one transaction
                '''
                    two transaction
                    1: first time, 2 : second time  
                    profit =  2sell - 2buy + 1sell -1buy
                    profit =  2sell -(2buy - 1sell + 1buy)
                    profit =  2sell - (2buy - (1sell - 1buy))
                    profit =  2sell - (2buy - 1profit)
                    To get Max profit
                    (2buy - 1profit) should be min
                '''
                second_buy = min(second_buy, curPrice - first_profit)  # total drop volume level
                final_profit = max(final_profit, curPrice - second_buy)  # maximum if sum of two transactions
            return final_profit
        else:
            return 0

test = Solution()
test_data = [3,3,5,0,0,3,1,4]
print(test.maxProfit(test_data),'\n')

test_data = [7,3,1,3,7]
print(test.maxProfit(test_data),'\n')


test_data = [1,2,3,4,5]
print(test.maxProfit(test_data),'\n')

test_data = [7,6,4,3,1]
print(test.maxProfit(test_data),'\n')