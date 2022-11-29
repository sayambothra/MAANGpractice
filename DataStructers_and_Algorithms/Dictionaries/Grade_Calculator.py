#Q10-(i) - Program to create grade calculator using python
# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }

def getAverage(marks):
    print(marks)
    total_mark=0
    for i in marks:
        total_mark+=i
        total_mark=float(total_mark)
    return total_mark/len(marks)

def calculate_average(students):
    assignment=getAverage(students["assignment"])
    test = getAverage(students["test"])
    lab = getAverage(students["lab"])
    total_score= ((0.1*assignment)+(0.7*test)+(0.2*lab))
    return total_score

def print_students_grade(student_list):
    total_class=0
    for i in student_list:
        average=calculate_average(i)
        print(type(average))
        total_class+=average
        print(i)
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("Average marks of "+i+" is : "+average)
        if average >=90:
            print("Letter Grade of "+i+" is : A")
        if average >=80 and average < 90:
            print("Letter Grade of "+i+" is : B")
        if average >=70 and average < 80:
            print("Letter Grade of "+i+" is : C")
        if average >=60 and average < 70:
            print("Letter Grade of "+i+" is : D")
    return total_class/len(student_list)

def print_class_average():
    total_class_average=print_students_grade()
    print("Class Average is :" + str(total_class_average))
    if total_class_average >=90:
        print("Letter Grade of the class is A")
    if total_class_average >=80 and total_class_average <90 :
        print("Letter Grade of the class is B")
    if total_class_average >=70 and total_class_average < 80:
        print("Letter Grade of the class is C")
    if total_class_average >=60 and total_class_average < 70:
        print("Letter Grade of the class is D")

students=[jack,james,dylan,jess,tom]

print_students_grade(students)
print_class_average()