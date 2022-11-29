def Median(li1,li2):
    mid1=len(li1)//2
    mid2=len(li2)//2
    return int(li1[mid1]+li2[mid2])//2


li1=[1,12,15,26,38]
li2=[2,13,17,30,45]
print(Median(li1,li2))