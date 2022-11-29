'''
Activity_Selection_problem: #TC:O(NlogN) , SC:O(1)
 - Sorting activities based on finish time
 - Select first activity from sorted array and print it
 - For all remaining activities:
    If the start time of this activity is greater or equal to the
    finish time of previously selected activity then select this activity and print it

'''
activities=[["A1",0,6],
            ["A2",3,4],
            ["A3",1,2],
            ["A4",5,8],
            ["A5",5,7],
            ["A6",8,9]]

def printMaxActivities(activities):
    activities.sort(key=lambda x:x[2])
    i=0
    firstA=activities[i][0]
    print(firstA)
    for j in range(len(activities)):
        if activities[j][1]>activities[i][2]:
            print(activities[j][0])
            i=j


printMaxActivities(activities)