#Q1 - Convert key-value list Dictionary to List of Lists
test_dict={'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}
test_dictl=[]
for key,val in test_dict.items():
    test_dictl.append([key]+val)
print(test_dictl)

#Q2 - Convert List to list of Dictionaries
test_list = ["Gfg", 3, "is", 8]
res=[]
key_list=["name","number"]
for i in range(0,len(test_list),2):
    res.append({key_list[0]:test_list[i],key_list[1]:test_list[i+1]})
print(res)

#Q3 - Convert Lists of List to Dictionary
from collections import OrderedDict
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res=OrderedDict()
for i in test_list:
    res[tuple(i[0:2])]=tuple(i[2:])
print(res)

#Q4 - Convert List of Dictionaries to List of Lists
test_list = [{"Gfg": 123, "best": 10}, {"Gfg": 51, "best": 7}]
res=[]
for keys,values in enumerate(test_list,start=0):
    if keys == 0:
        res.append(list(values.keys()))
        res.append((list(values.values())))
    else:
        res.append((list(values.values())))
print(res)

#Q5 - Convert key-values list to dictionary
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
res=OrderedDict(zip(test_dict['month'],test_dict['name']))
print(res)

#Q6 - Covert a list of tuples into Dictionary:
test_list= [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
di=OrderedDict()
for a,b in test_list:
    print(a,b)
    di.setdefault(a,[]).append(b)
print(di)

#Q8-Ways to Convert a string to dictionary
str=" Jan = January; Feb = February; Mar = March"

dict=OrderedDict(substring.split("=") for  substring in str.split(";"))
print(dict)

#Q9 - Convert dictionary to K sized dictionaries
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}
K = 3
count=0
dict1=OrderedDict()
res=[]
for key in test_dict:
    dict1[key] = test_dict[key]
    count+=1
    if count%K==0:
        res.append(dict1)
        dict1=OrderedDict()
        count=0
print(res)

#Q10 - Convert Matric to Dictionary
test_list=[[5,6,7],[8,3,2]]
count=1
dict1=OrderedDict()
for i in test_list:
    dict1[count]=i
    count+=1
print(dict1)

res={idx +1 : test_list[idx] for idx in range(len(test_list))}
print(res)






