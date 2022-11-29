def Equilibrium(li):
    for i in range(1,len(li)):
        leftSum=sum(li[0:i])
        rightSum=sum(li[i+1:])
        if leftSum == rightSum:
            return li[i]
    return -1

list1=[1,4,2,5,0]
print(Equilibrium(list1))