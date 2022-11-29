'''
House Robber
'''

def HouseRobber(houses,currentIndex):
    if currentIndex >=len(houses):
        return 0
    else:
        StealFirstHouse=houses[currentIndex]+HouseRobber(houses,currentIndex+2)
        SkipFirstHouse=HouseRobber(houses,currentIndex+1)
        return max(StealFirstHouse,SkipFirstHouse)

houses=[6,7,1,8,30,2,4]
print(HouseRobber(houses,0))