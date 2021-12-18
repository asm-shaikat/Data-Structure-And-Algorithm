n=int(input("How Many Activities? "))
print("Enter activities Starting and End Time in Separate Lines.")
activities=[]
for i in range(n):
    s,f=map(int,input("Activity %d: "% (i+1)).split())
    activities.append([s,f])
#a=[[3,1],[1,5],[7,5],[5,2]]
#sorted_item = sorted(a,key=lambda x : x[1])
#print(sorted_item)
sorted_item = sorted(activities,key= lambda x:x[1])
print(sorted_item)
a=[0]
i=0
for m in range(1,n):
    if sorted_item[m][0]>=sorted_item[i][1]:
         a.append(m)
         i=m
print("Selected Activites: ",end=' ')
for element in a:
          print(sorted_item[element],end=' ')
print("\nSelected Index:",a)

   
