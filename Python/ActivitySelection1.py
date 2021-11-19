NoOfActivity = int(input("How many activity: "))
print("Enter start time and finished time")
Array = []
selection=[0]
for i in range(NoOfActivity):
    x,y = map(int,input("Enter %d Activity: "%i).split())
    Array.append([x,y])
SortedArray = sorted(Array,key=lambda x:x[1])
q=0
for i in range(len(SortedArray)):
    if(SortedArray[i][0] >= SortedArray[q][1]):
        q=i
        selection.append(i)
print(selection)
