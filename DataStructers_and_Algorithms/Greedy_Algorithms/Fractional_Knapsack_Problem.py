'''
Fractional Knapsack Problem - TC:o(NlogN) , SC :O(1)
 -Calculate the denisty or ratio for each item
 - Sort items based on the ratio
 -Take items with the highest ratio sequentially until weight allows
 - Add the next item as much (fractional) as we can
'''
class Item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value /  weight

def FractionKnapsack(items,capacity):
    items.sort(key=lambda x:x.ratio,reverse=True)
    usedCapacity=0
    totalValue=0
    for i in items:
        if usedCapacity+i.weight <=capacity:
            usedCapacity+=i.weight
            totalValue+=i.value
        else:
            unusedweight=capacity-usedCapacity
            value=i.ratio*unusedweight
            usedCapacity+=unusedweight
            totalValue+=value
        if usedCapacity == capacity:
            break
    print("Total value : "+str(totalValue))

item1=Item(20,100)
item2=Item(30,120)
item3=Item(10,60)
cList=[item1,item2,item3]
FractionKnapsack(cList,50)