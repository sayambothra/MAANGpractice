# Implementing Temprature Question Using Arrays:
import numpy as np
No_of_Days=int(input('How many days temprature?'))
Tempratures=[]
total=0
count=0
for i in range(No_of_Days):
    day_temprature=float(input('Day '+str(i+1)+' Temprature'))
    Tempratures.append(day_temprature)
    total=total+day_temprature
average=total/No_of_Days
print('Average Tempratute: '+str(average))
for i in range(len(Tempratures)):
    if(Tempratures[i]>average):
        count=count+1
if count>1:
    print(str(count)+' days the temprature was above average')
else:
    print(str(count) + ' day the temprature was above average')

