def BSearch(li1,value):
    low=0
    top=len(li1)-1
    while low <= top:
        mid=int(low+top)//2
        if li1[mid] == value:
            return mid
        elif li1[mid] > value:
            top=mid-1
        elif li1[mid] <  value:
            low=mid + 1

list1=[10,20,30,50,60,80,110,130,140,170]
val=110
print(BSearch(list1,val))



