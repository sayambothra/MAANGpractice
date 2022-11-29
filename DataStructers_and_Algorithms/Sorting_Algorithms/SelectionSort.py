"""
In case of Selection Sort we Repeatedly find the minimum element and
move it into the sorted part of array to make unsorted part sorted
-It works well with small lists
TC:O(n^2),SC:O(1)
When to use Selection Sort ?
 - When we have insufficient memory
 - Easy to implement
When to avoid Selection sort ?
  - When time is a concern
"""

def SelectionSort(li):
    for i in range(0,len(li)):
        min_index = i
        for j in range(i+1,len(li)):
            if li[min_index]>li[j]:
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]
    return li



print(SelectionSort([2,7,1,6,3]))
