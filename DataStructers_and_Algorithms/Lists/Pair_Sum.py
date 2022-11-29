nums=[2,7,5,11,4]
total=9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==total:
            print([nums[i],nums[j]])


#Udemy Solution
def findPairs(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] == num[j]:
                continue
            elif num[i]+num[j] == target:
                print(i,j)
Mylist=[1,2,3,2,3,4,5,6]
findPairs(Mylist,6)



