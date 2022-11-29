def KandaneAlgorithm(li):
    max = 0
    summation=0
    for i in range(0,len(li)):
        for j in range(i,len(li)):
            summation=summation+li[j]
            #print(summation)
            if max < summation:
                max = summation
    return max

list1=[-2,-3,4,-1,-2,1,5,-3]
print(KandaneAlgorithm(list1))

