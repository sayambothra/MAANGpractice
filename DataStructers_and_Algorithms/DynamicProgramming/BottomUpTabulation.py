def fibTab(n):
    fibSer=[0,1]
    for i in range(2,n+1):
        fibSer.append(fibSer[i-1]+fibSer[i-2])
    return fibSer[n-1]

print(fibTab(6))