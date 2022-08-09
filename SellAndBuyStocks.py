
#  Buy and sell stocks problem is buying stocks on a certain day and selling it on a certain day to maximize the profit 
#  Also, the stocks must be sold on a day after the stocks was bought.  The index of the array represents the days and the elements of the list represents the price of the stock as at the given day.

#  This will require a two-pointer algo pattern

#  example : [ 2 4 1 ]

class Solution:
    def sell_and_buy_stocks(self,prices):
        left = right = prices[0]
        diff = 0
        for index in range(len(prices)):
            if prices[index] < left:
                left = right = prices[index]
            if prices[index] > left:
                right =  prices[index] 

                diff = max(diff,right-left)
        return diff 






if __name__ =='__main__':
    prices = list(map(int,input().rstrip().split()))

    solution= Solution()
    results= solution.sell_and_buy_stocks(prices)
    print(results)
    
    
    
