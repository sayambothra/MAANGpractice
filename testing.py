import random
def do_stuff(num=0):
    try:
        if num:
            return int(num)+5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err

#Exercixe
def guess(num):
    answer=random.randint(1,10)
    while True:
        try:
            if int(num) >0 and int(num)< 11:
                if num == answer:
                    print("You are a genius")
                    break
                else:
                    print('Try Again')
        except ValueError:
            print('please enter a Number')
            continue


