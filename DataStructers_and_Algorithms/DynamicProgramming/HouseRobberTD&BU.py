#House Robber Top-Down

def HouseRobberTD(houses,currentIndex,dp):
    if currentIndex >=len(houses):
        return 0
    else:
        if currentIndex not in dp:
            stealFirstHouse=houses[currentIndex]+HouseRobberTD(houses,currentIndex+2,dp)
            skipFirstHouse=HouseRobberTD(houses,currentIndex+1,dp)
            dp[currentIndex]=max(stealFirstHouse,skipFirstHouse)
        return dp[currentIndex]


houses=[6,7,1,30,8,2,4]
print(HouseRobberTD(houses,0,{}))
#House Robber Bottom Up:
def HouseRobberBU(houses,currentIndex):
    temArr=[0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):
        temArr[i]=max(houses[i]+temArr[i+2],temArr[i+1])
    return temArr[0]

print(HouseRobberBU(houses,0))
