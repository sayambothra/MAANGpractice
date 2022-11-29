#Zero one Knapsack - TD
class Item:
    def __init__(self,weight,profit):
        self.weight=weight
        self.profit=profit

def zoKnapsackTD(items, capacity, currentIndex,tempDict):
    dictKey=str(currentIndex) + str(capacity)
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[currentIndex]
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsackTD(items, capacity - items[currentIndex].weight,currentIndex+1,tempDict)
        profit2 = zoKnapsackTD(items, capacity, currentIndex+1,tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)
items=[mango,apple,orange,banana]
print(zoKnapsackTD(items,7,0,{}))

def ZoKnapSackBU(profits,weights,capacity):
    if capacity <=0 or len(profits) == 0 or len(weights) !=len(profits):
        return 0
    numberOfRows=len(profits)+1
    dp=[[0 for i in range(capacity+2)] for j in range(numberOfRows)]
    for row in range(numberOfRows-2,-1,-1):
        for column in range(1,capacity+1):
            profit1=0
            profit2=0
            if weights[row]<=column:
                profit1=profits[row]+dp[row+1][column-weights[row]]
            profit2=dp[row+1][column]
            dp[row][column] =max(profit1,profit2)
    return dp[0][capacity]

profits=[31,26,17,72]
weights=[3,1,3,5]
print(ZoKnapSackBU(profits,weights,7))

