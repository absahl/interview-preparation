"""
We're given an array of daily stock prices (integers for simplicity).
Return the buying and selling prices for making the maximum profit.

The values in the array represent the cost of stock each day.
As we can buy and sell the stock only once, we need to find the best buy and
sell prices that maximize profit (or minimized loss) over a given span of time.

We need to maximize the profit from a single buy and sell.
If we can't make any profit, we'll try to minimize the loss.
"""

def find_buy_sell_stock_prices(stock_nums):
    print('stock nums: {0}'.format(stock_nums))
    stock_nums_len = len(stock_nums)

    if stock_nums_len < 2:
        print(' invalid array length: {0}'.format(stock_nums_len))
        return (None, None)

    buy = 0
    sell = stock_nums_len - 1
    for i in range(1, stock_nums_len - 1):
        if stock_nums[i] < stock_nums[buy]:
            if i < sell:
                print(' updating buy to {0}'.format(i))
                buy = i
            elif stock_nums[stock_nums_len - 1] - stock_nums[i] > stock_nums[sell] - stock_nums[buy]:
                print(' updating buy to {0} and updating sell to {1}'.format(i, stock_nums_len - 1))
                buy = i
                sell = stock_nums_len - 1
        elif stock_nums[i] > stock_nums[sell]:
            print(' updating sell to {0}'.format(i))
            sell = i

    print(' result: {0}'.format((stock_nums[buy], stock_nums[sell])))
    return (stock_nums[buy], stock_nums[sell])

if __name__ == '__main__':
    #find_buy_sell_stock_prices([7, 1, 5, 0, 2, 3])
    #find_buy_sell_stock_prices([7, 1, 5, 3, 6, 4])
    find_buy_sell_stock_prices([1, 2, 3, 4, 3, 2, 1, 2, 5])
