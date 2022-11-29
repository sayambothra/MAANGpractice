# 1: Program to print half pyramid using *
n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print("* ",end="")
    print()
#2: Program to print half pyramid a using numbers
n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print(str(j)+" " ,end="")
    print()
#3: Program to print half pyramid using alphabets
n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(64+i)+" " ,end="")
    print()
#4: Inverted half pyramid using *
n= int(input())
for i in range(n-1,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
#5: Inverted half pyramid using numbers
n=int(input())
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(str(j)+" " ,end="")
    print()
#6: Floyd's Triangle
n=int(input())
number=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(number)+" " ,end="")
        number+=1
    print()
#7: Program to print full pyramid using *
n=int(input())
for i in range(1,n+1):
    k=0
    for j in range(1,(n-i)+1):
       # print(j,end="")
        print(" ",end=" ")
    while k<(2*i-1):
        print("* ",end="")
        k+=1
    print()
#8: Inverted full pyramid of *
n=int(input())
for i in range(n,0,-1):
    k=0
    for j in range(1,(n-i)+1):
       # print(j,end="")
        print(" ",end=" ")
    while k<(2*i-1):
        print("* ",end="")
        k+=1
    print()
#9: Full Pyramid of Numbers


