'''
Coin_Change_Problem - TC:O(N),SC:(1)
 -Find the biggest coin that is less than the given total number
 -Add Coin to the result and subtract coin from total number
 - If V is equal to Zero:
        then print result
    else:
        continue step 2 and 3
'''

def CoinChange(totalNumber,coins):
    N=totalNumber
    coins.sort()
    index=len(coins)-1
    while True:
        coinValue =coins[index]
        if N>=coinValue:
            print(coinValue)
            N=N-coinValue
        if N <coinValue:
            index-=1
        if N==0:
            break

coins=[1,2,5,20,50,100]
CoinChange(201,coins)