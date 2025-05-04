def profit(arr,days):
    profits = 0
    for i in range(1,days):
        if arr[i] > arr[i-1]:
            profits+=arr[i]-arr[i-1]
    return profits
stocks = [1,3,2,5]
profits = profit(stocks,len(stocks))
print(profits)