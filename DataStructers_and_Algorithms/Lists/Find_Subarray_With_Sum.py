list1=[1, 4, 0, 0, 3, 10, 5]
value=7
def SubArray(list1):
    for i in range(len(list1)):
        sum=0
        newList=[]
        sum=sum+list1[i]
        newList.append(list1[i])
        for j in range(i+1,len(list1)):
            print(j)
            print(sum)
            if(sum == value):
                print("Subarray found",newList)
                return newList
            else:
                sum=sum+list1[j]
                newList.append(list1[j])
                print(newList)


print(SubArray(list1))
