list1=[1, 4, 3, 2]
3 < 7 > 4 < 8 > 2 < 6 > 1
for i in range(0,len(list1)-1):
    if(i%2==0):
       
        if(list1[i]>list1[i+1]):
            temp=list1[i+1]
            list1[i+1]=list1[i]
            list1[i]=temp
    else:

        if(list1[i]<list1[i+1]):
            temp1 = list1[i + 1]
            list1[i + 1] = list1[i]
            list1[i] = temp1
print(list1)


