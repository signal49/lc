

#from json.tool import main
#from operator import index

# 121. Best time to buy and sell stock
# MEMory: O(1), Time Complexity: O(n)
class Solution:
    def maxProfit(prices) -> int:
        l, r = 0, 1 # left = buy, right=sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

    if __name__ ==  '__main__':
        arr = [7,1,5,3,6,4] 
        # input: [7,1,5,3,6,4] -> 5
        print(maxProfit(arr))

    




