def LargestNumber(li):
    for i in range(len(li)):
        li[i]=str(li[i])
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[j]+li[i]>li[i]+li[j]:
                li[i],li[j]=li[j],li[i]
    result=''.join(li)
    if (result=='0'*len(result)):
        return '0'
    else:
        return result

li1=[54,546,548,60]
print(LargestNumber(li1))

