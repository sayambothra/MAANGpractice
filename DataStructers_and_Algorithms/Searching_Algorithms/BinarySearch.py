"""
Binary Search:
 - Binary Search is Faster than Linear Search
 - Half of the remaining elements cab be eliminated at a time,instead of elimination them one by one
 - Binary Search only works for sorted arrays.

 TC:Worst-Case:O(logN),Best-Case:O(1)
 SC:O(1)

"""

def BinarySearch(li,value):
    low=0
    top=len(li)-1
    while low <= top:
        mid=int((low+top)/2)
        if li[mid] == value:
            return mid
        elif value < li[mid]:
            top=mid-1
        elif value > li[mid]:
            low=mid + 1


li=[1,2,3,4,5,6,7,8,9]
print(BinarySearch(li,7))
