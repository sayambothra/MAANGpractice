def ZeroSum(li):

    for i in range(0,len(li)):
        sumArray=li[i]
        nl=[li[i]]
        longL=[]
        for j in range(i+1,len(li)):
            sumArray=sumArray+li[j]
            print(sumArray)
            nl.append(li[j])
            print(nl)
            if sumArray == 0:
                print(nl)


    return longL

li=[15,-2,2,-8,1,7,10,23]
print(ZeroSum(li))