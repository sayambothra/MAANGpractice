def TrapWater(li):
    totalwater=0
    for i in range(0,len(li)-1):
        maxA=li[i]
        for j in range(0,i):
            maxA=max(maxA,li[j])
        maxB=li[i]
        for j in range(i+1,len(li)):
            maxB=max(maxB,li[j])
            totalwater=totalwater+(min(maxA,maxB)-li[i])
    return totalwater

li=[0,1,0,2,1,0,1,3,2,1,2,1]
print(TrapWater(li))