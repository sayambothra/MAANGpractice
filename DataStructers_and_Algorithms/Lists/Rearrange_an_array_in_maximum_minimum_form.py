myList=[1,2,3,4,5,6,7]
newList=[]
length=0
if(len(myList)%2==0):
    length=len(myList)
else:
    length=len(myList)+1
for i in range(length//2):
    if(myList[i]==myList[-(i+1)]):
        newList.append(myList[-(i+1)])
    else:
        newList.append(myList[-(i + 1)])
        newList.append(myList[i])
print(newList)