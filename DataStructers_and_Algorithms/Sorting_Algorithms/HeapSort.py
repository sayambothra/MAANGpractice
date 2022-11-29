"""
Heap Sort -
 - Insert data to Binary Heap Tree
 - Extract data from binary heap
 - It is best suited with array

TC:O(nlogn),SC:O(1)

"""
def heapify(li,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2

    if l < n  and li[l]<li[smallest]:
        smallest=l
    if r < n and li[r]<li[smallest]:
        smallest = r
    if smallest != i:
        li[i],li[smallest]=li[smallest],li[i]
        heapify(li,n,smallest)

def heapSort(li):
    n=len(li)
    for i in range(int(n/2)-1,-1,-1):
        heapify(li,n,i)
    for i in range(n-1,0,-1):
        li[i],li[0]=li[0],li[i]
        heapify(li,i,0)
    li.reverse()
    return li

li=[2,1,7,6,5,3,4,9,8]
print(heapSort(li))
