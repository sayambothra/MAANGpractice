n= int(input())
rows=2*n-1
columns=2*rows-1
for i in range(0,rows):
    for j in range(0,columns):
        No_of_Spaces=columns//2
        print(No_of_Spaces)
        while No_of_Spaces>=1:
            print("_",end="")
            No_of_Spaces-=1







