def SwappingPairs(A,B):
    sumA=sum(A)
    sumB=sum(B)
    avg=(sumA+sumB)/2
    diffA = int(abs(sumA-avg))
    diffB = int(abs(sumB-avg))
    print(diffA,diffB)
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            diffL=int(abs(A[i]-B[j]))
            print(diffL)
            if diffL == diffA:
                return A[i],B[j]


A=[5,7,4,6]
B=[1,2,3,8]
print(SwappingPairs(A,B))