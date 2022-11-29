#Q1-Display the Keys in sorted order
key_value={}
key_value[2] = '56'
key_value[1] = '2'
key_value[4] = '12'
key_value[5] = '24'
key_value[6] = '18'
key_value[3] = '323'
for i in sorted(key_value):
    print(i,end=" ")
print()

#Q2-Sort the dictionary by key
key_value1={}
key_value1['ravi'] = '10'
key_value1['rajnish'] = '9'
key_value1['sanjeev'] = '15'
key_value1['yash'] = '2'
key_value1['suraj'] = '32'
print(sorted(key_value1.items()))
for i in sorted(key_value1):
    print((i,key_value1[i]))

#Q3-Sorting the Keys and values in alphabetical using the value
key_value2={}
key_value2[2] = '56'
key_value2[1] = '2'
key_value2[4] = '12'
key_value2[5] = '24'
key_value2[6] = '18'
key_value2[3] = '323'
print(sorted(key_value2.items(),key=lambda kv:(kv[1],kv[0])))

#Q4- Sorting the dictionary using values:
dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
sort_values=sorted(dict.values())
print(sort_values)
dict_keys=list(dict.keys())
print(dict_keys)
sorted_dict={dict_keys[i]:sorted(dict.values())[i] for i in range(len(dict_keys))}
print(sorted_dict)

#Q5-(i)-Python dictionary with keys having multiple values
dict={}
x,y,z=10,20,30
dict[x,y,z]=x+y-z
x,y,z=5,2,4
dict[x,y,z]=x+y-z
print(dict)

#Q5-(ii)-Python dictionary with keys having multiple values
places={("19.07'53.2","72,54'51.0"):"Mumbai",
        ("28.33'34.1","77.06'16.6"):"delhi"}
long=[]
lat=[]
plc=[]
for i in places:
    long.append(i[0])
    lat.append(i[1])
    plc.append(places[i[0],i[1]])

print(long)
print(lat)
print(plc)

#Q6-(i)-Python program to find sum of all items in the dictionary:
myDict={'a':100,'b':200,'c':300}
print(sum(myDict.values()))
sum=0
# for i in range(3):
#     keys=input()
#     values=int(input())
#     myDict[keys]=values
#     sum+=int(values)
# print(sum)
# print(myDict)


#Q7-(i)-Get size of dictionary using getsizeof() method
import sys
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print("Size of dic1 : "+str(sys.getsizeof(dic1))+" bytes.")
print("Size of dic2 : "+str(sys.getsizeof(dic2))+" bytes.")
print("Size of dic3 : "+str(sys.getsizeof(dic3))+" bytes.")

#Q7-(ii)-Get size of dictionary using inbuilt __sizeof__() method
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print("Size of dic1 : "+str(dic1.__sizeof__())+" bytes.")
print("Size of dic2 : "+str(dic2.__sizeof__())+" bytes.")
print("Size of dic3 : "+str(dic3.__sizeof__())+" bytes.")

#Q8-(i) - Sorting a list using itemgetter
from operator import itemgetter

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(lis,key=itemgetter('age')))
print(sorted(lis,key=itemgetter('age','name')))
print(sorted(lis,key=itemgetter('age','name'),reverse=True))

#Q8-(i) - Sorting a list using itemgetter
print(sorted(lis,key=lambda i :(i['age'])))
print(sorted(lis,key=lambda i: (i['age'],i['name'])))
print(sorted(lis,key=lambda i :(i['age'],i['name']),reverse=True))

#Q9-(i) - Merging Python Dictionaries Using Update Method
Dict1={'a':1,'b':2}
Dict2={'c':3,'d':4}
print(Dict1.update(Dict2))
print(Dict1)

#Q9-(ii) - Merging Python Dictionaries Using **Expression
res={**Dict1,**Dict2}
print(res)

#Q9-(iii) - Merging Python Dictionaries Using | operator
res=Dict1|Dict2
print(res)

#Q9-(iv) - Merging Python Dictionaries Using loop and Keys Method
for i in Dict2.keys():
    Dict1[i]=Dict2[i]
print(Dict1)



#Q11-(i)- Insertion at the beginning in OrderedDict
from collections import OrderedDict
dict=OrderedDict([('akshat','1'),('nikhil','2')])
dict.update({'manjeet':'3'})
dict.move_to_end('manjeet',last=False)
print(dict)

#Q12-Check Order of character in string using input:
def CheckOrder(input,pattern):
    dict=OrderedDict.fromkeys(input)
    plen=0
    for keys,values in dict.items():
        if(keys == pattern[plen]):
            plen+=1
        if plen==len(pattern):
            return True
    return False

print(CheckOrder('enginegers rock','eg'))

#Find Common elements in sorted arrays by dictionary intersection
from collections import Counter
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
a1=Counter(ar1)
a2=Counter(ar2)
a3=Counter(ar3)
res_dict = OrderedDict(a1.items() & a2.items() & a3.items())
print(res_dict)
common=[]
for keys,values in res_dict.items():
        common.append(keys)
print(sorted(common,reverse=True))

#Q13- Dictionary and counter in Python to find winner of election
from collections import Counter
votes=["john", "johnny", "jackie",
        "johnny", "john", "jackie",
        "jamie", "jamie", "john",
        "johnny", "jamie", "johnny",
        "john"]

candidate_votes=Counter(votes)
dict={}
for i in candidate_votes.values():
     dict[i]=[]
for key,values in candidate_votes.items():
    dict[values].append(key)

maxVote=sorted(dict.keys(),reverse=True)[0]
if len(dict[maxVote])>1:
    print(sorted(dict[maxVote])[0])
else:
    print(dict[maxVote][0])

#Q14-Key with maximun unique values
test_dict = {"Gfg" : [5, 7, 5, 4, 5], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
max_val=0
max_key=None
for i in test_dict:
    if(len(set(test_dict[i])))>max_val:
        max_val=len(set(test_dict[i]))
        max_key=i
print(max_key)

#Q15-Find all duplicates in a string
input="geeksforgeeks"
lcounter=Counter(input)
for keys,values in lcounter.items():
    if values>1:
        print(keys,end=" ")

#Q16-Group similar items to Dictionary Values:
from collections import defaultdict
tlist=[4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
result=defaultdict(list)
for i in tlist:
    result[i].append(i)
print(result)

#Q18-Replace String by Kth Dictionary values
test_list=["Gfg","is","Best"]
repl_dict={"Gfg":[5,6,7],"is":[7,4,2]}
K=2
result=[]
result=[i if i not in repl_dict else repl_dict[i][K] for i in test_list]
#result=' '.join(result)
print(result)

#Q19-(i)-Ways to remove a key from dictionary-using del keyword
test_dict={"Arushi": 22, "Mani": 21, "Haritha": 21}
print(test_dict)
del test_dict['Mani']
print(test_dict)
#Q19-(ii)-Ways to remove a key from dictionary-using pop method
test_dict={"Arushi": 22, "Mani": 21, "Haritha": 21}
print(test_dict)
test_dict.pop('Mani')
print(test_dict)
#Q19-(iii)-Ways to remove a key from dictionary-using items() and dictionary comprehension
test_dict={"Arushi": 22, "Mani": 21, "Haritha": 21}
print(test_dict)
new_dict={key:val for key,val in test_dict.items() if key != 'Mani'}
print(new_dict)
#Q19-(iv)-Ways to remove a key from dictionary-using python dictionary comprehension
test_dict={"Arushi": 22, "Mani": 21, "Haritha": 21}
print(test_dict)
new_dict={key:test_dict[key]for key in test_dict if key != 'Mani'}
print(new_dict)
#Q19-(v)-Ways to remove a key from dictionary-Elemination and iteration
test_dict={"Arushi": 22, "Mani": 21, "Haritha": 21}
print(test_dict)
for key,cal in test_dict.items():
    if key!='Mani':
        print(key,cal)



#Q20-Replace words from Dictionary
test_str="geeksforgeeks best for geeks"
repl_dict={"best":"good and better","geeks":"all CS aspirants"}
temp_str=test_str.split()
res=[]
for word in temp_str:
    res.append(repl_dict.get(word,word))
res=' '.join(res)
print(test_str)
print(res)

#Q21-(i)-Remove Dictionary Key words
test_str = 'gfg is best for geeks'
# printing original string
print("The original string is : " + str(test_str))
# initializing Dictionary
test_dict = {'geeks': 1, 'best': 6}
temp_str=test_str.split()
re=[]
for i in test_dict:
    if i in temp_str:
        temp_str=test_str.replace(i," ")
print(temp_str)
#Q21-(ii)-Remove Dictionary Key words
test_str = 'gfg is best for geeks'
# printing original string
print("The original string is : " + str(test_str))
# initializing Dictionary
test_dict = {'geeks': 1, 'best': 6}
temp_str=test_str.split()
re=[]
for i in temp_str:
    if i not in test_dict.keys():
        re.append(i)
re=' '.join(re)
print(re)

#Q22 (i)-Remove all duplicates words from a given sentence
s="Python is great and Java is also great"
l=s.split()
k=[]
for i in l:
    if(s.count(i)>=1) and i not in k:
        k.append(i)
k=' '.join(k)
print(k)
#Q22-(ii)-Remove all duplicates words from a given sentence
from collections import Counter
s="Python is great and Java is also great"
m=s.split()
l=Counter(m)
t=" ".join(l.keys())
print(t)

#Q23-Remove duplicate values across Dictionary Values
test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}
# printing original dictionary
print("The original dictionary : " + str(test_dict))
c=Counter()
for val in test_dict.values():
    c.update(val)
res={val:[key for key in j if c[key] == 1]
        for val,j in test_dict.items()}
print(str(res))

#Q24 print mirror characters of a string
main="paradox"
org='abcdefghijklmnopqrstuvwxyz'
rev='zyxwvutsrqponmlkjihgfedcba'
dictChars=OrderedDict(zip(org,rev))
print(dictChars)
k=3
prefix=main[0:k-1]
suffic=main[k-1:]
mirror=''
for i in range(len(suffic)):
    mirror=mirror+dictChars[suffic[i]]
print(prefix+mirror)

#Q25 - Counting the frequinces in a list using dictionary:
mylist=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
freq={}
for i in mylist:
    freq[i]=mylist.count(i)
for key,values in freq.items():
    print("%d : %d"%(key,values))

#Q26 - Dictionary Values Mean:
my_dict={"Gfg":5,"is":10,"Best":15}
sum=0
for i in my_dict.values():
    sum=sum+i
print(sum/len(my_dict))

#Q26 - Python Counter and dictionary intersection example (Make a string using deletion and rearrangement)
s1="Hello"
s2="dnaKfhelddf"
s1count=Counter(s1)
s2count=Counter(s2)
res=s1count & s2count
print(res == s1count)
#Q27- Python dictionary,set and counter to check if frequencies can be same

#Q29 - Posiible words using given characters in python:
Dict=["go","bat","me","eat","goal","boy", "run"]
arr=['e','o','b', 'a','m','g', 'l']
res=[]
for i in Dict:
    count=0
    for j in range(len(i)):
        if i[j] in arr:
            count+=1

    if count==len(i):
        res.append(i)
print(res)


#Q30 -  Maximum record value key in a dictionary
test_dict = {'gfg': {'Manjeet': 5, 'Himani': 10},
             'is': {'Manjeet': 8, 'Himani': 9},
             'best': {'Manjeet': 10, 'Himani': 15}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))
# initializing search key
key = 'Himani'
res=None
max_rec=0
for i in test_dict:
    if test_dict[i][key]>max_rec:
        max_rec=test_dict[i][key]
        res=i
print(res)

#Q31- Extract values of a particular Key in nested Values:
test_dict = {'Gfg': {"a": 7, "b": 9, "c": 12},
             'is': {"a": 15, "b": 19, "c": 20},
             'best': {"a": 5, "b": 10, "c": 2}}
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
# initializing key
temp = "c"
res=[val[temp] for key,val in test_dict.items() if temp in val]
print(res)















