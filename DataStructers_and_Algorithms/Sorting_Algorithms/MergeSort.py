"""
Merge Sort
 - It is divide and conquer Algorithm
 - Divide the input array in two halves and we keep halving recursively until they become too small and cannot be broken further
 - Merge halves by sorting them

When to use Merge Sort?
  -When you need stable sort
  -When average expected time is O(NlogN)

When to avoid merge Sort?
 - When space is a concern

TC:O(NLogN),SC:O(N)
"""
def merge(cli,l,m,r):
    n1=m-l+1
    n2=r-m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0,n1):
        L[i]=cli[l+i]
    for j in range(0,n2):
        R[j]=cli[m+1+j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            cli[k] = L[i]
            i+=1
        else:
            cli[k] = R[j]
            j +=1
        k +=1
    while i < n1:
        cli[k] =L[i]
        i+=1
        k+=1
    while j < n2:
        cli[k] = R[j]
        j+=1
        k+=1

def MergeSort(li,l,r):
    if l < r:
        m=(l+(r-1))//2
        MergeSort(li,l,m)
        MergeSort(li,m+1,r)
        merge(li,l,m,r)
    return li



li=[2,1,7,6,5,3,4,9,8]
print(MergeSort(li,0,8))
