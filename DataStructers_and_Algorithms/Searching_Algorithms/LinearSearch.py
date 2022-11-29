"""
Linear Search :
TC:O(N),SC:O(1)
"""

def LinearSearch(li,value):
    for i in range(0,len(li)):
        if li[i] == value:
            return "Elemnt is Found at position : "+str(i)
        else:
            continue
    return "Element is not present in the list"

li=[2,1,7,4,5]
print(LinearSearch(li,4))