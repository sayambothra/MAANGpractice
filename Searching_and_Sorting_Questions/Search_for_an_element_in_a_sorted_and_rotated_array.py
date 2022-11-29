def RotatedArray(li,val):
    pivot=0
    for i in range(0,len(li)):
        if li[i] > li[i+1]:
            pivot =i
    li1=li[0:pivot]
    li2=li[pivot+1:len(li)]
    BinarySearch(li1,val)
    BinarySearch(li1,val)


def BinarySearch(li,val):
    low=0
    top=li-1
    while low <=top:
        mid=int(low+top)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            top=mid-1
        elif li[mid]<val:
            low=mid +1



