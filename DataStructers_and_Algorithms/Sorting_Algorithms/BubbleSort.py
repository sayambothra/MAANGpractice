"""
Bubble sort is also referef as Sinking Sort
We repeatedly compare each pair of adjacent items and swap them if they are in the wrong order
TC:O(n^2),SC:O(1)
When to use Bubble Sort?
- When the input is already Sorted
- Space is a concern
- Easy to Implement
When to avoid Bubble Sort?
  - Average Time Complexity is poor
"""
def BubbleSort(li):
    for i in range(0,len(li)-1):
        for j in range(len(li)-i-1):

             if li[j]>li[j+1]:
                 li[j], li[j + 1] = li[j + 1], li[j]
            #     temp=li[j]
            #     li[j]=li[j+1]
            #     li[j+1]=temp
    return li

print(BubbleSort([2,1,7,6,5,3,4,9,8]))
