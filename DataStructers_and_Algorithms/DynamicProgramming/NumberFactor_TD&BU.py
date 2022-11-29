#Number factor -Top Down Memoization

def NumFactTD(n,dp):
    if n in(0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        if n not in dp:
            subP1=NumFactTD(n-1,dp)
            subP2=NumFactTD(n-3,dp)
            subP3=NumFactTD(n-4,dp)
            dp[n]=subP1+subP2+subP3
        return dp[n]

print(NumFactTD(5,{}))

#Number Factor - Bottom Up

def NumFactBU(n):
    tb=[1,1,1,2]
    for i in range(4,n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]

print(NumFactBU(5))
