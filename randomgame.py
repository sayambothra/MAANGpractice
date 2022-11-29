import random
uNum=input("Enter a number between 1-10")
#rNum= random.randint(sys.argv[1],sys.argv[2])
rNum = random.randint(1, 10)
print(rNum)
while True:
    uNum = input("Enter a Number between 1- 10:   ")
    try:
        if int(uNum)>0 and int(uNum)<11:
        # if 0 <int(uNum) < 11:
            if int(uNum)==int(rNum):
                print("Congratulations")
                break
            else:
                continue
        print("Hard Luck try again!!")
    except ValueError:
        print("please enter a number")
        continue

